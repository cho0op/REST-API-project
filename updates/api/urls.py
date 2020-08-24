from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'updates_url'

urlpatterns = [
    path('', views.UpdateListAPIView.as_view()),
    path('<int:_id>/', views.UpdateDetailAPIView.as_view())
]
