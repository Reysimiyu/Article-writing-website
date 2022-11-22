from django.contrib import admin
from .models import Member, Category,Profile
# Register your models here.
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Profile)