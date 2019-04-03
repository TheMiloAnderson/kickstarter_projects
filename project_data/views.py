from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import Project

# Create your views here.
def project_list_view(request):
    projects=get_list_or_404(Project,id__lte=15)
    context= {
        'projects': projects,
    }
    return render(request, 'project_list.html',context)