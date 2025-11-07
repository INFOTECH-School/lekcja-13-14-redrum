from django.shortcuts import render
from .forms import ZgloszenieForm
from .models import Turniej
from django.contrib.auth.decorators import login_required
from .forms import AvatarForm
from django.contrib import messages
from .models import Zgloszenie, Profile
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



@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Znajdź wszystkie zgłoszenia użytkownika po e-mailu
    user_zgloszenia = Zgloszenie.objects.filter(email=request.user.email)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Avatar został zaktualizowany ✅")
    else:
        form = AvatarForm(instance=profile)

    return render(
        request,
        'profil.html',
        {'user': request.user, 'form': form, 'zgloszenia': user_zgloszenia}
    )