from django.contrib import admin
from .models import Sweet
# Register your models here.

@admin.register(Sweet)
class AdminSweet(admin.ModelAdmin):

    list_display=["title","timestamp" ,"updated"]