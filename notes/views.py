from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Note
# Create your views here.
def home(request):
    notes = Note.objects.all()
    return render(request,'notes/home.html',{'notes':notes})



def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')


        Note.objects.create(
            title = title,
            content = content
        )


        return redirect('home')
    
    return render(request,'notes/add_note.html')

def delete_note(request , id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('home')


def edit_note(request,id):
    note = Note.objects.get(id = id)
    if request.method == "POST":
        
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('home')
    return render(request,'notes/edit_note.html',{'note': note})