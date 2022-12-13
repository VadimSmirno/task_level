
from django.views import generic
from .models import Task

class TaskList(generic.ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'list_task'

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'detail_task.html'
    context_object_name = 'detail_task'
