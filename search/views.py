import csv,io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView
import json
from .models import WordModel


# View method for uploading .tsv file in to database
@permission_required('admin.can_add_log_entry')
def upload_file(request):
    '''
    View method to upload a .tsv file to database.
    '''
    template='form.html'
    prompt={
        'order':'Order of TSV should be word and its rank'
    }
    if request.method == 'GET':
        return render(request,template,prompt)

    tsv_file=request.FILES['file']
    if not tsv_file.name.endswith('.tsv'):
        messages.error(request,'This is not a tsv file')
    data_set=tsv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    for column in csv.reader(io_string,delimiter="\t",quotechar="|"):
        _,created=WordModel.objects.update_or_create(
                word=column[0],
                rank=column[1]
        )
    context={}
    return render(request,template,context)



def search(request):
    '''
    View method to search a word given by user and print first 25 results of that search.
    '''
    queryset_list=WordModel.objects.order_by('-rank')
    query=request.GET.get('q',None)
    if query is not None:
        word_list=queryset_list.filter(word__icontains=request.GET['q'])
        words=[]
        if len(word_list)>25:
            for i in range(25):
                words.append(word_list[i])
        else:
            words=word_list
    else:
        words=None
    context={
        'word_list':words,
        'word':request.GET.get('q',None)
    }
    return render(request,'search.html',context)
