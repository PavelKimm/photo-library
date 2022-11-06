from django.contrib import admin

from photos.models import Photo

admin.autodiscover()
# disabling sidebar in admin panel
admin.site.enable_nav_sidebar = False

admin.site.register(Photo)
