from django.urls import path
from .views import CustomUserListCreateAPIView, CustomUserRetrieveUpdateDestroyAPIView, CustomUserLoginAPIView, RoomListAPIView, RoomDetailAPIView

urlpatterns = [
    path('register/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('login/', CustomUserLoginAPIView.as_view(), name='login'),
    # chat related urls
    path('rooms/', RoomListAPIView.as_view(), name='room-list'),
    path('rooms/<slug:slug>/', RoomDetailAPIView.as_view(), name='room-detail'),
]
