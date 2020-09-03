from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def landing_page(request, *args, **kwargs):
    return render(request, 'landing-page.html', {'portal':'LANDING PAGE'})

def redirectToPatientLogin(request, *args, **kwargs):
    print('BLAH BLAH BLAH')
    return redirect('http://localhost:8000/login/patient')
