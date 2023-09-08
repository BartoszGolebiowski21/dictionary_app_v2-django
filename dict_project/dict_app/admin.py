from django.contrib import admin

from .models import Word, Page

# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_filter = ("remaining_repetitions",)


admin.site.register(Word, WordAdmin)
admin.site.register(Page)