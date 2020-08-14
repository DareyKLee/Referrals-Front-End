from django.shortcuts import render

# Create your views here.

def patientLogin(request):
    return render(request, 'login-page.html', {'portal':'PATIENT'});


def clinicLogin(request):
    return render(request, 'login-page.html', {'portal':'CLINIC'});