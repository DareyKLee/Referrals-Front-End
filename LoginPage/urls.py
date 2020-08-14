from django.urls import path

from . import views

urlpatterns = [
    path('login/patient', views.patientLogin, name='patient login'),
    path('login/clinic', views.clinicLogin, name='clinic login')
]