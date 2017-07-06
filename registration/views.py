from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from .forms import UserForm
from registration.models import User

def basic_info(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            # process data in form.cleaned_data as required
            print(request.POST['first_name'])
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserForm()

    return render(request, 'basic_info.html', {'form': form})

def user_registration(request):
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['first_name_text'])
        return redirect('/user_registration/')

    profiles = User.objects.all()
    return render(request, 'user_registration.html', {'profiles': profiles})

def thanks(request):
    return render(request, 'thanks.html')
