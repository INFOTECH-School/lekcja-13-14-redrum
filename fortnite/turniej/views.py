from django.shortcuts import render
from .forms import ZgloszenieForm
from .models import Turniej

def zapisz_sie(request):
    if request.method == 'POST':
        form = ZgloszenieForm(request.POST)
        if form.is_valid():
            turniej = form.cleaned_data['turniej']
            if turniej.zgloszenia.count() < turniej.liczba_graczy:
                form.save()
                return render(request, 'potwierdzenie.html')
            else:
                return render(request, 'blad.html')
    else:
        turniej_id = request.GET.get('turniej')
        if turniej_id:
            try:
                turniej = Turniej.objects.get(pk=turniej_id)
                form = ZgloszenieForm(initial={'turniej': turniej})
            except Turniej.DoesNotExist:
                form = ZgloszenieForm()
        else:
            form = ZgloszenieForm()

    return render(request, 'zapis.html', {'form': form})



def lista_turniejow(request):
    turnieje = Turniej.objects.all()
    return render(request, 'turniej.html', {'turnieje': turnieje})