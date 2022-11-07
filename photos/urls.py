from django.urls import path
from photos.views import PhotoListView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, UserPhotoListView

urlpatterns = [
    # path('', home, name='home-page'),
    path('', PhotoListView.as_view(), name='home-page'),
    path('profile/', UserPhotoListView.as_view(), name='profile'),
    path('photos/new/', PhotoCreateView.as_view(), name='photo-create'),
    path('photos/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
]
