from django.shortcuts import render, HttpResponse, redirect
from TpFinalBioApp.forms import SecuenceForm

# Create your views here.


def home(request):
    return render(request,"TpFinalBioApp/home.html")

def map(request):
    return render(request,"TpFinalBioApp/map.html")

def upload(request):
    if request.method == 'POST':
        form = SecuenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = SecuenceForm()
    return render(request,"TpFinalBioApp/upload.html", {

        'form': form
    })