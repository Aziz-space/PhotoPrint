from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import ServiceForm, SizeForm, OrderForm, ImageUploadForm, RegisterForm, ChangeProfileForm, OIForm
from PhotoPrint.models import Service, SI, Order, OI, Status
from .forms import ChangePasswordForm 
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse



def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})

def workspace_view(request):
    services = Service.objects.all()
    return render(request, 'workspace/index.html', {'services': services})





def add_service(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES)
        size_form = SizeForm(request.POST)
        
        if service_form.is_valid() and size_form.is_valid():
            service = service_form.save()
            size = size_form.save(commit=False)
            size.service = service
            size.save()
            return redirect('index')  
    else:
        service_form = ServiceForm()
        size_form = SizeForm()
    
    return render(request, 'workspace/add_service.html', {
        'service_form': service_form,
        'size_form': size_form
    })

def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    sizes = SI.objects.filter(service=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        size_forms = [SizeForm(request.POST, prefix=str(size.id), instance=size) for size in sizes]

        if form.is_valid() and all([sf.is_valid() for sf in size_forms]):
            service = form.save()

            for size_form in size_forms:
                size_form.save()
            
            return redirect('index')
    else:
        form = ServiceForm(instance=service)
        size_forms = [SizeForm(prefix=str(size.id), instance=size) for size in sizes]


    if not size_forms:
        size_forms = [SizeForm]

    return render(request, 'workspace/update_service.html', {
        'form': form,
        'size_forms': size_forms  
    })




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})

def login_profile(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_profile(request):
    logout(request)
    return redirect('index') 




@login_required(login_url='/workspace/login/')
def profile(request):
    form = ChangeProfileForm(instance=request.user)

    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно изменен')
            return redirect('/workspace/')

    return render(request, 'auth/profile.html', {'form': form})


@login_required(login_url='/workspace/login/')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user) 
                messages.success(request, 'Пароль успешно изменен.')
                return redirect('profile')
            else:
                form.add_error('old_password', 'Неверный старый пароль.')
    else:
        form = ChangePasswordForm()

    return render(request, 'auth/change_password.html', {'form': form})


def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        service.delete()
    return redirect('index')









def get_current_order(request):
    order_id = request.session.get('order_id')

    if order_id:
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            pass

    order = Order.objects.create()
    request.session['order_id'] = order.id
    return order







def upload_image(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        service = Service.objects.create(title="New Service", image=image)
        
        return JsonResponse({'image_url': service.image.url})
    return JsonResponse({'error': 'Image not uploaded'}, status=400)











def order_status_view(request):
    return render(request, 'order_status.html', {})



def create_oi(request):
    if request.method == 'POST':
        form = OIForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload') 
    else:
        form = OIForm()
    return render(request, 'prices.html', {'form': form})


def upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'index'))
    return redirect(request.META.get('HTTP_REFERER', 'index'))