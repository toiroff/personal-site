from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import AboutMe,Project
from .forms import ContactForm
# Create your views here.
def index(request):
  about = AboutMe.objects.first()
  form = ContactForm()
  project = Project.objects.all()

  if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index')


  content = {'about':about,
             'form':form,
             'project':project}
  return render(request,'index.html',content)


def project(request,pk):
    project = Project.objects.get(id=pk)
    about = AboutMe.objects.first()

    content = {'project':project,'about':about}
    return render(request,'project.html',content)

