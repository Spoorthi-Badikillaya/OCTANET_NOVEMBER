from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm 
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmailAuthenticationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app import models

from app.models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'app/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('tasks')  # Redirect to the dashboard or any other page after registration.
        else:
            print(form.errors)  # Add this line to print errors to the console
            messages.error(request, "Registration failed. Please check the form data.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'app/home.html', {'form': form})

class CustomLoginView(LoginView):
    template_name='app/login_template.html'
    fields= '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')
class TaskList(LoginRequiredMixin,ListView):
    model= Task
    context_object_name='tasks'
    def get_queryset(self):
        # Filter tasks by the currently logged-in user
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a count of incomplete tasks for the current user
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

    
class TaskDetail(LoginRequiredMixin, DetailView):
    model=Task
    context_object_name='task'
    template_name='app/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model=Task
    fields = ['title', 'description', 'complete']
    success_url= reverse_lazy('tasks')
    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields = ['title', 'description', 'complete']
    success_url= reverse_lazy('tasks')
class DeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url= reverse_lazy('tasks')