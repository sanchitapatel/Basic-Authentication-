
from django.contrib import admin
from .models import MovieModel,StudentModel

# Register your models here.
#@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
admin.site.register(MovieModel)

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','city']