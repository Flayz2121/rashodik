from django import forms
from .models import Kursy

class KursyModelForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['poSpisku', 'naLitso', 'naryad','bolnye','uvolnenie','otpusk']