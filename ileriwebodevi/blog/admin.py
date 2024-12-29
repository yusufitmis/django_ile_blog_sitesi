from django.contrib import admin
from .models import PostModel, Comment

# PostModel için Admin paneli düzenlemesi
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')  # Görünürdeki alanlar
    search_fields = ('title', 'content')  # Başlık ve içerikte arama yapma
    list_filter = ('date_created', 'author')  # Tarihe ve yazara göre filtreleme
    ordering = ('-date_created',)  # Son eklenenler önce gelir

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)
