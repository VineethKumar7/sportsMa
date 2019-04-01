from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Appadmin1.forms import UserRegForm,UserRegForm2,PlayerRegForm,TournmentDetails
from django.contrib.auth.models import User
from .models import UserProfile,Player,Tournament,Awards
from django.contrib.auth.decorators import user_passes_test

# URL '' name='index'
def userindex(request):
    return render(request, "club/index1.html", {})

# URL 'playerreg' name='player'
def playerreg(request):
    if request.method == 'POST':
        preg_form=PlayerRegForm(data=request.POST)
        if preg_form.is_valid():
            preg = preg_form.save()
            return render(request, "club/successful.html",{'form':preg_form})
    else:
            preg_form=PlayerRegForm()
    return render(request, 'club/playerreg.html',
    {'form':preg_form})



def mainReg_view(request):
    if request.method == 'POST':
        reg_form=UserRegForm(data=request.POST)
        reg2_form=UserRegForm2(data=request.POST)
        if reg_form.is_valid() and reg2_form.is_valid():
            reg = reg_form.save()
            reg.set_password(reg.password)
            reg.save()
            reg2 = reg2_form.save(commit=False)
            reg2.user = reg
            return HttpResponseRedirect(reverse('index'))
    else:
            reg_form=UserRegForm()
            reg2_form=UserRegForm2()
    return render(request, 'club/user_reg.html',
    {'form1':reg_form, 'form2':reg2_form})

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
    high= Tournament.objects.get(eventname= "High Jump")
    long= Tournament.objects.get(eventname= "Long Jump")
    javelin= Tournament.objects.get(eventname= "Javelin")
    shortput= Tournament.objects.get(eventname= "Shortput")
    meter= Tournament.objects.get(eventname= "100 meter")
    return render(request, 'club/tournament.html', {'long':long,'high':high,'javelin':javelin,
                                                        'shortput':shortput,'meter':meter })


# URL 'contact' name='contact'
def contact(request):
    return render(request, 'club/contact.html')

# URL 'awa' name='awa'
def awa(request):
    high= Awards.objects.get(eventname= "High Jump")
    long= Awards.objects.get(eventname= "Long Jump")
    javelin= Awards.objects.get(eventname= "Javelin")
    shortput= Awards.objects.get(eventname= "Shortput")
    meter= Awards.objects.get(eventname= "100 meter")
    return render(request,'club/awards.html', {'long':long,'high':high,'javelin':javelin,
                                                        'shortput':shortput,'meter':meter })

# URL 'signin' name='signin'
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user:
            print("Username and password are correct")
            if user.is_active:
                login(request,user)
                print("Logged in")
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('adminD:admin_D'))
                else:
                    return HttpResponseRedirect(reverse('index'))
        else:
            print("Check the username and password")
    else:
         return render(request,'club/login1.html')

def loggedlist(request):
    queryset = Users.objects.all()
    context_dict = {
        'loggedlist' : queryset,
    }
    return render(request, "loggedlist.html", context_dict)

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
