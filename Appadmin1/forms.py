from django import forms
from .models import Player,Tournament

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
