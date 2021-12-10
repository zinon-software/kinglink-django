from django.contrib import admin

from group.models import Category, Group, Sections

# Register your models here.
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Sections)