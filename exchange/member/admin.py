from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = [ "last_name", "first_name", "ski_area", "base" ]


admin.site.register(Member, MemberAdmin)