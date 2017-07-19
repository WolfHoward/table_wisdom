from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

from .forms import SignUpForm

def basic_info(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'basic_info.html', {'form': form})

def home(request):
    return render(request, 'home.html')

# def user_registration(request):
#     if request.method == 'POST':
#         User.objects.create(first_name=request.POST['first_name_text'])
#         return redirect('/user_registration/')
#
#     profiles = User.objects.all()
#     return render(request, 'user_registration.html', {'profiles': profiles})
#
def confirmation(request):
    return render(request, 'confirmation.html')
