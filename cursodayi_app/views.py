from django.shortcuts import get_object_or_404, render,redirect
from .forms import PersonForm
from .models import Person


# Create your views here.
def index(request):
    persons = Person.objects.all()
    print(persons)
    return render (request, 'index.html', {'persons':persons})

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonForm()
    return render(request, 'index.html', {'form': form})

def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('index')
    return render(request, 'index.html', {'person': person} )

def update_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonForm(instance=person)
    return render(request, 'update_person.html', {'form': form})

