from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.conf import settings
from django.views.generic import DetailView, ListView


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


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        project_list = get_list_or_404(Project)
        paginator = Paginator(project_list, 20)
        page = self.request.GET.get('page')
        return paginator.get_page(page)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['projects'] = Project.objects.filter(id < 5)
    #     return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'


def project_detail_view(request, pk=None):
    context = {
        'project': get_object_or_404(Project, id=pk)
    }
    return render(request, 'project_detail.html', context)
