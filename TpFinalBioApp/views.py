from django.shortcuts import render, HttpResponse, redirect
from TpFinalBioApp.forms import SecuenceForm
import json
# Create your views here.


def home(request):
    return render(request,"TpFinalBioApp/home.html")

def map(request):

    markers = [{"titulo": 'En este lugar vive Lucio', "latitude": -34.7430435,"longitude": -58.25890429999998},
              {"titulo": 'En este lugar vive Emiliano', "latitude": -34.719658,"longitude": -58.255364}
            ]

    json_string = json.dumps(markers)
    return render(request,"TpFinalBioApp/map.html",{'markers': json_string})

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