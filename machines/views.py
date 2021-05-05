from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Machine
from .forms import MachineForm


# Create your views here.

def index(request):
    machines = Machine.objects.order_by('-pk')
    context = {
        'machines': machines,
    }
    return render(request, 'machines/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.save()
            return redirect('machines:detail', machine.pk)

    else:
        form = MachineForm()
    context = { 'form': form }
    return render(request, 'machines/create.html', context)


def detail(request, pk):
    machine = get_object_or_404(Machine, pk=pk) 
    context = {'machine': machine}
    return render(request, 'machines/detail.html', context)


def delete(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.user.is_authenticated:
        machine.delete()
        return redirect('machines:index')
    return redirect('machines:detail', machine.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machines:detail', machine.pk)

    else:
        form = MachineForm(instance=machine)

    context = {
        'form': form,
        'machine': machine,
    }
    return render(request, 'machines/update.html', context)
