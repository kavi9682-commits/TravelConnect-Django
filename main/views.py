from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm

def home(request):
    featured = Destination.objects.order_by('-rating')[:3]
    return render(request, 'home.html', {'featured': featured})

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'destination_form.html', {'form': form, 'title': 'Add Destination'})

def edit_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destination_form.html', {'form': form, 'title': 'Edit Destination'})

def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')
    return render(request, 'confirm_delete.html', {'destination': destination})
