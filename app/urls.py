from django.urls import path
from .views import index, project

urlpatterns = [
  path('',index, name="index"),
  path('project/<int:pk>/',project,name="project")
]