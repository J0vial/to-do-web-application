from contextlib import redirect_stderr
from django.urls import reverse
from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db import models

def homepage(request):
    return render(request, 'main/home.html')

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'main/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        status = self.request.GET.get('status')
        upcoming = self.request.GET.get('upcoming')
        if status in ['pending', 'completed']:
            queryset = queryset.filter(status=status)
        if upcoming == '1':
            queryset = queryset.filter(due_date__gte=timezone.now().date())
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                models.Q(title__icontains=q) | models.Q(description__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Task.objects.filter(user=self.request.user)
        context['total_tasks'] = user_tasks.count()
        context['completed_tasks'] = user_tasks.filter(status='completed').count()
        context['pending_tasks'] = user_tasks.filter(status='pending').count()
        context['overdue_tasks'] = user_tasks.filter(status='pending', due_date__lt=timezone.now().date()).count()
        context['in_progress_tasks'] = user_tasks.filter(status='pending', due_date__gte=timezone.now().date()).count()
        return context

@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('main:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('main:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main/task_confirm_delete.html'
    success_url = reverse_lazy('main:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@login_required
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = 'completed' if task.status == 'pending' else 'pending'
    task.save()
    return HttpResponseRedirect(reverse('main:task_list'))
