from django.shortcuts import render

# sociotorcedor/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import SocioTorcedor
from .forms import SocioTorcedorForm

def lista_socios(request):
    socios = SocioTorcedor.objects.all()
    return render(request, 'sociotorcedor/lista_socios.html', {'socios': socios})

def cadastrar_socio(request):
    if request.method == 'POST':
        form = SocioTorcedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioTorcedorForm()
    return render(request, 'sociotorcedor/cadastrar_socio.html', {'form': form})

def editar_socio(request, pk):
    socio = get_object_or_404(SocioTorcedor, pk=pk)
    if request.method == 'POST':
        form = SocioTorcedorForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioTorcedorForm(instance=socio)
    return render(request, 'sociotorcedor/editar_socio.html', {'form': form, 'socio': socio})

def excluir_socio(request, pk):
    socio = get_object_or_404(SocioTorcedor, pk=pk)
    socio.delete()
    return redirect('lista_socios')
