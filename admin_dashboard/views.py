from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Appadmin1.forms import UserRegForm,UserRegForm2,PlayerRegForm,TournmentDetails
from django.contrib.auth.models import User
from Appadmin1.models import UserProfile,Player,Tournament,Awards
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
class tlistView(LoginRequiredMixin,ListView):
    content_object_name ='tournament_list'
    model = Tournament
    template_name = 'admin/tour_list.html'
class plistView(LoginRequiredMixin,ListView):
    content_object_name ='player_list'
    model = Player
    template_name = 'admin/player_list.html'

class alistView(LoginRequiredMixin,ListView):
    content_object_name ='awards_list'
    model = Awards
    template_name = 'admin/awards_list.html'

class tlistUpdate(LoginRequiredMixin,UpdateView):
    fields = ('eventname', 'venue', 'date', 'time')
    model = Tournament
    template_name = 'admin/tour_form.html'

class plistUpdate(LoginRequiredMixin,UpdateView):
    fields = ('firstname', 'middlename', 'lastname', 'location','eventname' )
    model = Player
    template_name = 'admin/tour_form.html'

class alistUpdate(LoginRequiredMixin,UpdateView):
    fields = ('eventname', 'first', 'second', 'third' )
    model = Awards
    template_name = 'admin/tour_form.html'

class plistDelete(LoginRequiredMixin,DeleteView):
    model =Player
    success_url = reverse_lazy("adminD:player_list")
    template_name = 'admin/player_confirm_delete.html'

# URL 'dashboard' name='admin_D'
@login_required
def adminD(request):
    if request.user.is_superuser:
        return render(request, "admin/admin_dashboard.html", {})
    else:
        return HttpResponse("You don't have permission to access this page")
