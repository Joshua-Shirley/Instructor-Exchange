from django.contrib import admin
from .models import Member, Ski_Area

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = [ "last_name", "first_name" ]
    ordering = ["last_name", "first_name"]

class Ski_Area_Admin(admin.ModelAdmin):
    list_display = ["name", "location"]
    ordering = ["name"]

admin.site.register(Member, MemberAdmin)
admin.site.register(Ski_Area, Ski_Area_Admin)