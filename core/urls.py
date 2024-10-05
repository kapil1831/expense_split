from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('expenses/', views.expense_list, name='expenses'),
]