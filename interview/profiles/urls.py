from django.urls import path
from .views import (
    RegisterView,
    UserProfileListCreateAPIView,
    UserProfileDetailAPIView
)

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("userprofiles/", UserProfileListCreateAPIView.as_view()),
    path("userprofiles/<int:pk>/", UserProfileDetailAPIView.as_view()),
]
