from django.shortcuts import render, redirect
from .models import Service
from workspace.forms import ServiceForm  

def index(request):
    services = Service.objects.prefetch_related('sizes').all()
    return render(request, 'index.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ServiceForm()
    return render(request, 'workspace/add_service.html', {'form': form})



def prices(request):
    return render(request, 'prices.html')