from django.contrib import admin
from .models import Yangiliklar,Image
from unfold.admin import ModelAdmin

class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Yangiliklar)
class YangiliklarAdmin(ModelAdmin):
    inlines = [ImageInline]
    list_display = ('sarlavha', 'date', 'main_image')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)
