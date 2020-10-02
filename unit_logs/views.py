from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Unit
from .forms import UnitForm

@login_required
def index(request):
    """The home page for unit logs"""
    return render(request, 'unit_logs/index.html')

@login_required
def units(request):
    """Show all units"""
    units = Unit.objects.order_by('-date_added')
    context = {'units': units}
    return render (request, 'unit_logs/units.html', context)

def winx(request):
    """Show all winx"""
    units = Unit.objects.order_by('date_added')
    context = {'units': units}
    return render (request, 'unit_logs/winx.html', context)

def enable(request):
    """Show all enable"""
    units = Unit.objects.order_by('date_added')
    context = {'units': units}
    return render (request, 'unit_logs/enable.html', context)

def arkle(request):
    """Show all arkle"""
    units = Unit.objects.order_by('date_added')
    context = {'units': units}
    return render (request, 'unit_logs/arkle.html', context)


def denman(request):
    """Show all denman"""
    units = Unit.objects.order_by('date_added')
    context = {'units': units}
    return render (request, 'unit_logs/denman.html', context)

def kauto(request):
    """Show all kauto"""
    units = Unit.objects.order_by('date_added')
    context = {'units': units}
    return render (request, 'unit_logs/kauto.html', context)

def frankel(request):
    """Show all frankel"""
    units = Unit.objects.order_by('date_added')
    context = {'units': units}
    return render (request, 'unit_logs/frankel.html', context)

@login_required
def unit(request, unit_id):
    """Show a single unit"""
    unit = Unit.objects.get(id=unit_id)
    context = {'unit': unit}
    return render(request, 'unit_logs/unit.html', context)

@login_required
def new_unit(request):
    """Add a new unit"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = UnitForm()
    else:
        # POST data submitted; process data
        form = UnitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_unit.html', context)

@login_required
def edit_unit(request, unit_id):
    """Edit an existing unit"""
    unit = Unit.objects.get(id=unit_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current unit
        form = UnitForm(instance=unit)
    else:
        # POST data submitted; process data
        form = UnitForm(instance=unit, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:index', unit_id=unit.id)

        context = {'unit': unit, 'form': form}
        return render(request, 'unit_logs/edit_unit.html', context)

@login_required
def show_unit(request, unit_pk):
    unit = get_object_or_404(Unit, pk=unit_pk)
    if request.method == 'GET':
        form = UnitForm(instance=unit)
        return render(request, 'unit_logs/show_unit.html', {'unit':unit, 'form':form})
    else:
        try:
            form = UnitForm(request.POST, instance=unit)
            form.save()
            return redirect('unit_logs:index')
        except ValueError:
            return render(request, 'unit_logs/edit_unit.html', {'unit': unit, 'form': form, 'error': 'Bad info'})

@login_required
def delete_unit(request, unit_pk):
    unit = get_object_or_404(Unit, pk=unit_pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('unit_logs:index')