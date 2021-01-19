from django.urls import path,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home/',views.HomeView,name='home'),
    path('add/',views.AddNew.as_view(),name='add_new'),
    path('all/', views.PasswordsView.as_view(),name='all'),
    path('detail/<int:pk>/',views.PasswordDetailView.as_view(),name='detail'),
]
