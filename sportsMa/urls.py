"""sportsMa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import Appadmin1.views
import admin_dashboard.urls
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Appadmin1.views.userindex, name='index'),
    path('playerreg/',Appadmin1.views.playerreg, name='player'),
    path('dashboard/',include('admin_dashboard.urls', namespace = "adminD")),
    path('about/', Appadmin1.views.about, name='about'),
    path('tour/',Appadmin1.views.tour2,name='tour'),
    path('contact/', Appadmin1.views.contact,name='contact'),
    path('awa/', Appadmin1.views.awa, name='awa'),
    path('signin/', Appadmin1.views.signin, name='signin'),
    path('customReg/', Appadmin1.views.mainReg_view, name='registration'),
    path('logout/', Appadmin1.views.user_logout, name='logout'),

]
