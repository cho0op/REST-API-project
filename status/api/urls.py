from django.urls import path
from status.api import views

urlpatterns = [
    path('', views.StatusListAPIView.as_view()),
    path('<int:id>/', views.StatusDetailAPIView.as_view()),
    path('create/', views.StatusCreateAPIView.as_view()),
    # path('<int:status_id>/update/', views.StatusUpdateAPIView.as_view()),
    # path('<int:status_id>/delete/', views.StatusUpdateAPIView.as_view()),
]
