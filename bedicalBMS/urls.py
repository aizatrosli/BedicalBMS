"""bedicalBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from bedical.views import *

urlpatterns = [
    path('', mainpage, name='home'),
    path('appointment/', appointmentpage, name='appointment'),
    path('support/', supportpage, name='support'),
    path('dashboard/', dashboardpage, name='dash'),
    path('login/', loginpage, name='login'),
    path('profile/', profilepage, name='profile'),
    path('search/', searchpage, name='search'),
    path('patient/<uuid:bid>/', patientprofile, name='patientprofile'),
    path('staff/<uuid:bid>/', staffprofile, name='staffprofile'),
    path('admission/', admissionpage, name='admission'),
    path('patients/', patientpage, name='patient'),
    path('discharge/', dischargepage, name='discharge'),
    path('register/', registerpage, name='register'),
    url('', include('bedical.urls')),
    path('admin/', admin.site.urls),
]
