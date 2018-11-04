from django.contrib import admin
from .models import Photographer,Image,location,category

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('location','category')
admin.site.register(Photographer)
admin.site.register(Image)
admin.site.register(location)
admin.site.register(category)
