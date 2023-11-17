"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from app.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('task/<int:pk>/', TaskDetail.as_view() ,name='task'),
    path('tasks', TaskList.as_view() ,name='tasks'),
    path('task-create/', TaskCreate.as_view() ,name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view() ,name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view() ,name='task-delete'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
