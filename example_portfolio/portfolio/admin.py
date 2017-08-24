from django.contrib import admin
from .models import Work, CategoryWork


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'pub_date', 'client', 'location', 'category',)
    list_filter = ('title', 'pub_date', 'client', 'location', 'category',)


class CategoryWorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Work, WorkAdmin)
admin.site.register(CategoryWork, CategoryWorkAdmin)