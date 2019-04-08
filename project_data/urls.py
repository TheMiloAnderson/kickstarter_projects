from django.urls import path
from .views import project_list_view, project_detail_view, ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('<int:pk>', ProjectDetailView.as_view(), name='project_detail')
]
