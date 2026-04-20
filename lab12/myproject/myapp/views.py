from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request,'index.html',{"all_person":all_Person})

def about(request):
     return render(request,'about.html')

def form(request):
    if request.method == "POST":
     
        name_input = request.POST.get("name")
        age_input = request.POST.get("age")

        new_person = Person.objects.create(
            name=name_input,
            age=age_input
        )
   
        return redirect("/")
    else:
        return render(request, "form.html")

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        person.name = name
        person.age = age
        person.save()

        return redirect("/")
    else:
        return render(request, "edit.html", {"person": person})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")
