from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Appadmin1.forms import PlayerRegForm,TournmentDetails
from .models import Users, Login,Player,Tournament,Awards
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# URL '' name='index'
def userindex(request):
    return render(request, "club/index1.html", {})

# URL 'playerreg' name='player'
def playerreg(request):
    if request.method == 'POST':
        preg_form=PlayerRegForm(data=request.POST)
        if preg_form.is_valid():
            preg = preg_form.save()
            return render(request, 'club/admin_pannel.html',{'form':preg_form})
    else:
            preg_form=PlayerRegForm()
    return render(request, 'club/playerreg.html',
    {'form':preg_form})

# URL 'about' name='about'
def about(request):
    return render(request, "club/about.html",{})

# # URL 'tour' name='tour'
# def tour(request):
#     t = Tournament.objects.all()
#     template = loader.get_template("club/tournament.html")
#     context = {"t":t}
#     return HttpResponse(template.render(context,request))
#
# # URL 'tour2' name='tour2'
# def tour2(request):
#     tour=TournmentDetails()
#     return render(request, 'club/tournament2.html', {'form':tour})

# URL 'tour2' name='tour2'
def tour2(request):
    return render(request, 'club/tournament.html', {})


# URL 'contact' name='contact'
def contact(request):
    return render(request, 'club/contact.html')

# URL 'awa' name='awa'
def awa(request):
    return render(request,'club/awards.html')

# URL 'signin' name='signin'
def signin(request):
    return render(request,'club/login1.html')

# URL 'customReg' name='registration'
def custregForm(request):
    if request.method == 'POST':
        type = request.POST.get("type")
        first_name = request.POST.get('firstname')
        middle_name = request.POST.get('middlename')
        last_name = request.POST.get('lastname')
        address = request.POST.get('address')
        mobile = request.POST.get('num')
        location = request.POST.get('loc')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if type=="user":
            login = Login()
            login.email = email
            login.user_role = type
            login.password = password
            login.save()

        reg = Users()
        reg.firstname = first_name
        reg.middlename = middle_name
        reg.lastname = last_name
        reg.address = address
        reg.mobile = mobile
        reg.location = location
        reg.gender = gender
        #reg.email=email
        #reg.password=password
        reg.login=login
        reg.save()
        return render(request, 'club/login1.html')
    else:

        return render(request, 'club/user_reg.html')
