from django.db import models

class Turniej(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nazwa


class Zgloszenie(models.Model):
    turniej = models.ForeignKey(Turniej, on_delete=models.CASCADE, related_name='zgloszenia')
    nick = models.CharField(max_length=100)
    epic_id = models.CharField(max_length=100)
    email = models.EmailField()
    platforma = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nick} ({self.turniej.nazwa})"
