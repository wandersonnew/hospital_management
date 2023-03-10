from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def recursos_humanos(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home/index.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

def home(request):
    return render(request, 'home/index.html', {})