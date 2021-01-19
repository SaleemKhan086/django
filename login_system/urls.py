from django.urls import path,include
from django.views.generic import TemplateView
from .views import SignUpView

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('login_successfull/',TemplateView.as_view(template_name="login_system/login_successfull.html"),name="login_successfull" ),
    path('sign_up/',SignUpView.as_view(),name="sign_up"),
]
