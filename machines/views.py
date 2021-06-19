from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Machine
from .forms import MachineForm

def main(request):
    machines = Machine.objects.order_by('-pk')
    context = {
        'machines': machines,
        'menu': '목공기계',
    }

    return render(request, 'machines/main.html', context)

    
def index(request):
    machines = Machine.objects.order_by('-pk')
    context = {
        'machines': machines,
        'menu': '목공기계',
    }
    return render(request, 'machines/index.html', context)

def filter(request, category='all'):
    if category == 'all':
        machines = Machine.objects.order_by('-pk')
    elif category =='신품 기계' or category == '중고 기계':
        machines = Machine.objects.filter(category=category).order_by('-pk')
    else:
        return redirect('machines:index')
    context = {
        'machines': machines,
        'menu': '목공기계({})'.format(category[:2]),
    }
    return render(request, 'machines/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST, request.FILES)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.user = request.user 
            machine.save()
            return redirect('machines:detail', machine.pk)
    else:
        form = MachineForm()
    context = {
        'form': form,
        'menu': '목공기계',
        }
    return render(request, 'machines/create.html', context)


def detail(request, pk):
    machine = get_object_or_404(Machine, pk=pk) 
    context = {
        'machine': machine,
        'menu': '목공기계',
        }
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
        form = MachineForm(request.POST, request.FILES, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machines:detail', machine.pk)
    else:
        form = MachineForm(instance=machine)

    context = {
        'form': form,
        'machine': machine,
        'menu': '목공기계',
    }
    return render(request, 'machines/update.html', context)
