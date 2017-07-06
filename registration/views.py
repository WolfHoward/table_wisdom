from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def user_registration(request):
    return render(request, 'user_registration.html', {
        'new_discipline_text': request.POST.get("discipline_text", ""),
    })
