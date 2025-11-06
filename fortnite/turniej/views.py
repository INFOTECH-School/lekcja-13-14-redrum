from django.shortcuts import render
from .forms import ZgloszenieForm

def zapisz_sie(request):
    if request.method == 'POST':
        form = ZgloszenieForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'potwierdzenie.html')
    else:
        form = ZgloszenieForm()

    return render(request, 'zapis.html', {'form': form})
