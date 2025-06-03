from django.http import HttpResponse
from django.template import loader
from .models import Member, Ski_Area

# Create your views here.

def member_list(request):
    members = Member.objects.all().values()
    template = loader.get_template("members.html")
    context = {
        'member_list' : members
    }
    return HttpResponse(template.render(context, request))

def resort_list(request):
    resorts = Ski_Area.objects.all().values()
    template = loader.get_template("resorts.html")
    context = {
        "resort_list" : resorts
    }
    return HttpResponse(template.render(context, request))