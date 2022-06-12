from django.shortcuts import render, redirect
from django.views import generic as views

# Create your views here.
from denis.my_cv.models import Certificate, Denislav, Language, Project, ContactData, Work


class MainPage(views.TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        certificats = Certificate.objects.all()
        contact= ContactData.objects.first()
        languages = Language.objects.all()
        projects = Project.objects.all()
        works = Work.objects.all()
        denislav = Denislav.objects.first()
        mode=Denislav.objects.first().mode

        context['certificats']=certificats
        context['contact']=contact
        context['languages']=languages
        context['projects']=projects
        context['works']=works
        context['denislav']=denislav
        context['mode']=mode
        return context


def en_mode(request):
    deni=Denislav.objects.first()
    deni.mode=True
    deni.save()
    return redirect('index')

def de_mode(request):
    deni = Denislav.objects.first()
    deni.mode = False
    deni.save()
    return redirect('index')
