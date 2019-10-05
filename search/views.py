import csv,io
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import FileForm
from .models import WordModel

@permission_required('admin.can_add_log_entry')
def upload_file(request):
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
