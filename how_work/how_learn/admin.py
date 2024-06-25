from django.contrib import admin
from .models import ModelContent

# admin.site.register(ModelContent)

@admin.register(ModelContent)
class ModelAdmin234(admin.ModelAdmin):
    list_display=['id', 'name', 'content']



