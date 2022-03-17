from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Main(View):
    def get(self, request):
        return render(request, 'main.html')