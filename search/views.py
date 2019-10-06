import csv,io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView
from django.db.models.functions import Length
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
        'order':'Order of TSV should be word and its frequency'
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
                frequency=column[1]
        )
    context={}
    return render(request,template,context)



def search(request):
    '''
    View method to search a word given by user and print first 25 results of that search.
    '''
    queryset_list=WordModel.objects.order_by('-frequency')
    query=request.GET.get('q',None)
    if query is not None:
        word_list=queryset_list.filter(word__icontains=request.GET['q'])[:25]
        word_list=sorted(word_list,key=lambda o:(len(o.word),o.frequency))
        words=[]
        # Arrange the results using startswith method.
        for obj in word_list:
            if obj.word.startswith(query):
                words.append(obj)
        for obj in word_list:
            if obj not in words:
                words.append(obj)

    else:
        words=None
    context={
        'word_list':words,
        'word':request.GET.get('q',None)
    }
    return render(request,'search.html',context)
