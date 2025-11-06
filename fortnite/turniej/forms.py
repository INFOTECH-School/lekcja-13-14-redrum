from django import forms
from .models import Zgloszenie, Turniej
from django.db.models import Count, F

class ZgloszenieForm(forms.ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ['turniej', 'nick', 'epic_id', 'email', 'platforma']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['turniej'].queryset = (
            Turniej.objects.annotate(liczba_zgloszen=Count('zgloszenia'))
            .filter(liczba_zgloszen__lt=F('liczba_graczy'))
        )