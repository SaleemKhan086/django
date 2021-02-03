from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from .models import Task
# Create your views here.
class todoView(LoginRequiredMixin,View):
    def get(self,request):
        form = TaskForm()
        task_list = Task.objects.all().filter(owner=request.user)
        ctx = dict({'form':form, 'task_list':task_list})
        return render(request,"todo/todo.html",context=ctx)
    def post(self,request):
        form = TaskForm(request.POST)
        if not form.is_valid():
            return render(request,"todo/todo.html",{'form':form})
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        return self.get(self.request)
