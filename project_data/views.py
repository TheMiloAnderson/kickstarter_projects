from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.conf import settings


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def project_list_view(request):
    project_list = get_list_or_404(Project)
    paginator = Paginator(project_list, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)
    context = {
        'projects': projects,
    }
    return render(request, 'project_list.html', context)


def project_detail_view(request, pk=None):
    return render(request, 'project_detail.html')
