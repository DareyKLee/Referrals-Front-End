from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def landing_page(request, *args, **kwargs):
    return render(request, 'landing-page.html', {'portal':'LANDING PAGE'})

def redirectToPatientLogin(request, *args, **kwargs):
    return redirect('http://localhost:8000/login/patient')

def redirectToClinicLogin(request, *args, **kwargs):
    return redirect('http://localhost:8000/login/clinic')