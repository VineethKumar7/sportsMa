from django import forms
from .models import Player,Tournament,UserProfile
from django.contrib.auth.models import User

class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','first_name','last_name')

class UserRegForm2(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('mobile','location','gender')


class PlayerRegForm(forms.ModelForm):
    class Meta():
        model = Player
        fields = ('firstname','middlename','lastname','location','eventname')

class TournmentDetails(forms.ModelForm):

    class Meta():
        model = Tournament
        fields = ('eventname','venue','date','time')

        widgets = {
            'date': forms.SelectDateWidget(
                 empty_label=("Choose Year", "Choose Month", "Choose Day"),
            ),
            'time': forms.TimeInput(format='%H:%M'),
        }
