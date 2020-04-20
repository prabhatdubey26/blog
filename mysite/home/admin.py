from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactDisplay(admin.ModelAdmin):
    list_display=["sno","name","email","phone","content",  "timestamp"]
    list_filter = ["sno","name","email","phone"]

admin.site.register(Contact,ContactDisplay)