from unicodedata import name
from django.urls import path
from .views import TaskDetail, TaskList,TaskDetail,TaskCreate,TaskUpadte,DeleteView,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name= 'task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpadte.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(),name='task-delete'),
    path('login/',CustomLoginView.as_view(),name='Login'),
    path('logout/',LogoutView.as_view(next_page='Login'),name='Logout'),
    path('register/',RegisterPage.as_view(), name='Register'),

]