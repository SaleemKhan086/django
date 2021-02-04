from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
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
        if request.is_ajax():
            print("RECEIVED SELECT AJAX POST REQUEST....")
            id=request.POST['id']
            deleteRequest = request.POST['delete']
            task = Task.objects.get(pk=id)
            if deleteRequest=='false':
                task.finished = not task.finished
                task.save()
            else:
                task.delete()
            return JsonResponse({"success":True})
        form = TaskForm(request.POST)
        if not form.is_valid():
            return render(request,"todo/todo.html",{'form':form})
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        return self.get(self.request)
