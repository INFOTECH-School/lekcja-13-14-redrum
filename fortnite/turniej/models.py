from django.db import models

PLATFORMY = [
    ('PC', 'Komputer'),
    ('XBOX', 'Xbox'),
    ('PS', 'PlayStation'),
    ('SWITCH', 'Nintendo Switch'),
]


class Turniej(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    data = models.DateField(null=True, blank=True)
    liczba_graczy = models.IntegerField(max_length=3)
    aktualna_liczba = models.IntegerField(max_length=3)
    nagroda_pieniezna = models.IntegerField(max_length=6)

    def __str__(self):
        return self.nazwa


class Zgloszenie(models.Model):
    turniej = models.ForeignKey(Turniej, on_delete=models.CASCADE, related_name='zgloszenia')
    nick = models.CharField(max_length=100)
    epic_id = models.CharField(max_length=100)
    email = models.EmailField()
    platforma = models.CharField(max_length=20, choices=PLATFORMY, default='PC')

    def __str__(self):
        return f"{self.nick} ({self.turniej.nazwa})"
