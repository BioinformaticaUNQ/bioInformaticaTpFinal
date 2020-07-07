from Bio import SeqIO
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from TpFinalBioApp.forms import SecuenceForm
import json
# Create your views here.
from TpFinalBioApp.handler import handle_uploaded_file
from TpFinalBioApp.models import Secuence
import gmplot
import re




def home(request):
    return render(request,"TpFinalBioApp/home.html")

def map(request):
    #markers = [{"titulo": 'En este lugar vive Lucio', "latitude": -34.7430435,"longitude": -58.25890429999998},
    #          {"titulo": 'En este lugar vive Emiliano', "latitude": -34.719658,"longitude": -58.255364}]
    #json_string = json.dumps(markers)
    data = [('En este lugar vive Lucio', -34.7430435, -58.25890429999998,'http://i.stack.imgur.com/g672i.png'), 
            ('En este lugar vive Emiliano', 41.197855, 16.594981,'http://i.stack.imgur.com/g672i.png')
            ]
    list = [{"titulo": x[0], "latitude": x[1], "longitude": x[2],"arbol": x[3]} for x in data]
    json_string = json.dumps(list)
    return render(request,"TpFinalBioApp/map.html",{'markers': json_string})

def upload(request):
    if request.method == 'POST':
        form = SecuenceForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            form.save()
            return redirect('UploadedSecuence')
    else:
        form = SecuenceForm()
    return render(request,"TpFinalBioApp/upload.html", {

        'form': form
    })


def uploaded_secuence(request):
    done = True
    path = 'secuences/secuence.fasta'
    fasta_sequences = SeqIO.parse(open(path, 'r'), 'fasta')
    seq_dict = {rec.id : rec.seq for rec in fasta_sequences}
    for x, y in seq_dict.items():
        seqobj = re.search(r'gi.(\d*).gb.(\w*.\d*)',x)
        if seqobj.group(1) != '' and seqobj.group(2) != '' and x.count("|") == 4 and y != '':
            print(x)      
        else:
            done = False
            break
            

    if done:
        for fasta in fasta_sequences:
            fasta_to_insert = Secuence()
            fasta_to_insert.bio_id = fasta.id
            fasta_to_insert.content = fasta.seq
            fasta_to_insert.length = len(fasta.seq)
            fasta_to_insert.save()
        messages.success(request, f"El archivo se ha subido correctamente")
        return render(request, "TpFinalBioApp/uploaded_secuence.html", {'fasta_sequences': fasta_sequences})
    else:
        messages.error(request, f"El archivo no es correcto")
        return redirect('Home')
        

def convertDirectionToCoordinates(self, direction):
    apikey = 'AIzaSyAqJwGQtaGHY5Bm56dMzfcRgRRQ9uCn8G8'
    return gmplot.GoogleMapPlotter.geocode(direction, apikey=apikey)