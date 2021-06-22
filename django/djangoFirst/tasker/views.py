from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="new task")
    # priority = forms.IntegerField(label="priority", min_value=1, max_value=10)


def index(request):

    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request, 'tasker/index.html', {
        'tasks':request.session["tasks"]})

def add(request):

    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasker:index") )
        else:
            return render(request, "tasks/add.html", {
                "form":form
            })

    return render(request, 'tasker/add.html', {
        "form": NewTaskForm()    
    })