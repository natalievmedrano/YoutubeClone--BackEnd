from django.urls import path, include
from comments import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.add_comment),
    path('video/<str:video_id>/', views.get_comments_for_video),
    path('<int:pk>/', views.get_comment_by_id)
]
