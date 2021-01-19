from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views import View
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.
class LoginView(View):
    def get(self,request):
        next_url = reverse_lazy('login_successfull')
        ctx = {'next':next_url}
        return render(request,"registration/login.html",{})


    #def post(self,request):
    #    return render(request,"login_system/login_successfull.html",{})

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,"login_system/sign_up.html",{'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            print("not valid...")
            return render(request,"login_system/sign_up.html",{'form':form})
        #if p!=cp:
        #    form.add_error("confirm_password","passwords don't match")
        #    return render(request,"login_system/sign_up.html",{'form':form})
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        
        try:
            user = User.objects.create_user(username,email,password)
        except:
            form.add_error("email","This email is already linked to another account")
            return render(request,"login_system/sign_up.html",{'form':form})

        user.save()
        return redirect(reverse_lazy('login'))
