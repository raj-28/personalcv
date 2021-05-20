from django.shortcuts import render
from .models import FilesAdmin, Contactform
import os
from django.http import HttpResponse,Http404
from django.conf import settings
# Create your views here.
def index(request):
    context = {'file':FilesAdmin.objects.all()}
    if request.method=="POST":
        contact = Contactform()
        name = request.POST.get('name')
        email = requests.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.text = text
        contact.save()
        return HttpResponse("<h2>Thank You For Your Interest<h2>")
    return render(request, 'index.html', context)

def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/resumeupload")
            response['content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404

