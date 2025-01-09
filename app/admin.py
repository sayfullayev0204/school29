from django.contrib import admin
from .models import Yangiliklar,Image,Olimpiada
from unfold.admin import ModelAdmin
from parler.admin import TranslatableAdmin
class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Yangiliklar)
class YangiliklarAdmin(TranslatableAdmin, ModelAdmin):
    inlines = [ImageInline]
    list_display = ('sarlavha', 'date', 'main_image')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

@admin.register(Olimpiada)
class OlimpiadaAdmin(ModelAdmin):
    list_display = ('Yil','Fan')
