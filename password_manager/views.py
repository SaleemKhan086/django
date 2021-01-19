from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from .models import Password
from .forms import RecordForm

from cryptography.fernet import Fernet
# Create your views here.
@login_required(login_url='login')
def HomeView(request):
    return render(request,'password_manager/home.html',{})

class PasswordsView(ListView):
    template_name = 'password_manager/all.html'
    model = Password
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

class PasswordDetailView(DetailView):
    template_name= 'password_manager/detail.html'
    model=Password
    def decrypt(self,password):
        key = b't9tU7f2LS0svmx5YLhUAicgEaQZuqQAo9Ku9OLJAGTs='
        cipher_suite = Fernet(key)
        plain_text = cipher_suite.decrypt(password.encode('ascii'))
        return plain_text.decode('ascii')
    def get_context_data(self,**kwargs):
        data=super().get_context_data(**kwargs)
        obj = data['password']
        obj.password = self.decrypt(obj.password)
        data['object']=obj
        data['password']=obj
        return data

class AddNew(View):
    def encrypt(self,password):
        key = b't9tU7f2LS0svmx5YLhUAicgEaQZuqQAo9Ku9OLJAGTs='
        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(password.encode('ascii'))
        return ciphered_text.decode('ascii')

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,'password_manager/not_logged_in.html',{})
        form= RecordForm()
        return render(request,'password_manager/add_new.html',{'form':form})
    def post(self,request):
        form = RecordForm(request.POST)

        if not form.is_valid():
            return render(request,'password_manager/add_new.html',{'form':form})
        obj = form.save(commit=False)
        obj.password= self.encrypt(obj.password)
        obj.owner=request.user
        obj.save()
        return redirect(reverse_lazy('password_manager:home'))
