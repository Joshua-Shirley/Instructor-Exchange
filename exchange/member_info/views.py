
"""
# here is an example of checking for authentication  without the library
# EXAMPLE 1 - Singular
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class ProfileView(View):

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=401)
        return render(request, 'accounts/profile.html')
"""

# EXAMPLE 2 - global
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

class ProfileView(View):

    def get(self, request):
        return render(request, 'accounts/profile.html')

"""
# EXAMPLE 3 - decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

@login_required
class ProfileView(View):  
    def get(self, request):
        return render(request, 'accounts/profile.html')
""" 