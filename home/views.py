from django.shortcuts import render,redirect
from home.models import *
from home.forms import *
# Create your views here.


def home(request):
    abc = mainmenu.objects.all()
    xyz = submenu.objects.all()
    return render(request, 'home.html', {'m':abc,'mm':xyz})


def contact(request):
    form = contactform(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect(home)
    return render(request, 'contact.html')