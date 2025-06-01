from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def member_list(request):
    members = Member.objects.all().values()
    template = loader.get_template("members.html")
    context = {
        'member_list' : members
    }
    return HttpResponse(template.render(context, request))

