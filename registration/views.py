from django.shortcuts import redirect, render

from registration.models import User

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        User.objects.create(discipline=request.POST['discipline_text'])
        return redirect('/user_registration/')

    profiles = User.objects.all()
    return render(request, 'user_registration.html', {'profiles': profiles})
