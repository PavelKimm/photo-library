from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from photos.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/home.html'
    context_object_name = 'photos'
    ordering = ['-id']
    paginate_by = 3


class UserPhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'users/profile.html'
    context_object_name = 'photos'
    paginate_by = 3

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user).order_by('-id')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    # this view uses 'photo_form.html' template
    model = Photo
    fields = ['file', 'caption']

    def form_valid(self, form):
        # assign current user as author
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ['file', 'caption']

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.author or self.request.user.is_staff:
            return True
        return False


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = '/'

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.author or self.request.user.is_staff:
            return True
        return False
