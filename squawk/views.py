from django.shortcuts import render
from .models import squawk as squawk_model
from .forms import SquawkForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def Home(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'about.html')

def Squawk_list(request):
    if(request.method == "GET" and 'q' in request.GET):
        query = request.GET.get('q', '')
        squawks = squawk_model.objects.filter(content__icontains=query).order_by('-created_at')
        return render(request, 'squawk_list.html', {'squawks': squawks, 'query': query})
    return render(request, 'squawk_list.html', {'squawks': squawk_model.objects.all().order_by('-created_at')})

@login_required
def Squawk_create(request):
    if request.method == 'POST':
        form = SquawkForm(request.POST, request.FILES)
        if form.is_valid():
            new_squawk = form.save(commit=False)
            new_squawk.user = request.user
            new_squawk.save()
            return redirect('squawk:index')
    else:
        form = SquawkForm()
    return render(request, 'squawk_form.html', {'form': form})

@login_required
def Squawk_edit(request, squawk_id):

    squawk = get_object_or_404(squawk_model, id=squawk_id, user = request.user)

    if request.method == 'POST':
        form = SquawkForm(request.POST, request.FILES, instance=squawk)
        if form.is_valid():
            form.save()
            return redirect('squawk:index')
    else:
        form = SquawkForm(instance=squawk)
    return render(request, 'squawk_form.html', {'form': form})

@login_required
def Squawk_delete(request,squawk_id):
    squawk = get_object_or_404(squawk_model, id=squawk_id, user=request.user)
    if request.method == 'POST':
        squawk.delete()
        return redirect('squawk:index')
    return render(request, 'squawk_confirm_delete.html', {'squawk': squawk})


def logout(request):
    auth_logout(request)
    return redirect('squawk:index')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('squawk:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'form':form})