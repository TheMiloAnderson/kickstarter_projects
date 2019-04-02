from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
from django.core.paginator import Paginator


def project_list_view(request):
    project_list = get_list_or_404(Project)
    paginator = Paginator(project_list, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)
    context = {
        'projects': projects,
    }
    return render(request, 'project_list.html', context)
