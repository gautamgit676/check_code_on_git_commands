from django.urls import path
from app import views

urlpatterns = [
   path('demo/', views.MyView.as_view(), name='demo')   
]
     