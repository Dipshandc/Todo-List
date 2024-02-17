from django.urls import path
from . import views

urlpatterns = [
    path('detail/<pk>',views.TaskDetail.as_view(),name='detail'),
    path('list/',views.Tasklist.as_view(),name='list')
]