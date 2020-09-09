from django.urls import path
from status.api import views

urlpatterns = [
    path('', views.StatusAPIView.as_view()),
    path('<int:pk>/', views.StatusAPIDetailView.as_view()),
    # path('create/', views.StatusCreateAPIView.as_view()),
    # path('<int:pk>/update/', views.StatusUpdateAPIView.as_view()),
    # path('<int:pk>/delete/', views.StatusDeleteAPIView.as_view()),
]
