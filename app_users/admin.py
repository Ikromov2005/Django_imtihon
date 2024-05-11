from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Note
from .models import Student, Book, Hobby

User = get_user_model()

admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Hobby)



@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_filter = ['created', 'updated']
    list_display = ['title', 'is_done']
    list_display_links = ['title']
    list_editable = ['is_done']
    list_per_page = 100
    ordering = ['created', 'updated', 'title']
    save_on_top = True