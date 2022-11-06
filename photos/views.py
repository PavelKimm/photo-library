from django.shortcuts import render

from photos.models import Photo


def home(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos
    }
    return render(request, 'photos/home.html', context)


def profile(request):
    context = {'title': 'Profile'}
    return render(request, 'photos/profile.html', context)
