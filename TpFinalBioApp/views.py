import json
import os
import re
from subprocess import Popen, PIPE

from Bio.Align.Applications import ClustalwCommandline
import gmplot
from Bio import SeqIO, AlignIO
from django.contrib import messages
from django.shortcuts import render, redirect
from Bio.Alphabet.IUPAC import *


from TpFinalBioApp.forms import SecuenceForm
# Create your views here.
from TpFinalBioApp.handler import handle_uploaded_file
from TpFinalBioApp.models import Secuence


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


def secuencia_alineada(file):
    return True


def uploaded_secuence(request):
    done = True
    error_message = ''
    path = 'secuences/secuence.fasta'
    file = open(path, 'r')
    is_aligned = False

    if not file.readlines()[0].startswith('>'):
        error_message = 'la primera linea del archivo no inicia como un fasta >'
        messages.error(request, f"El archivo no es correcto. " + error_message)
        return redirect('Home')
    else:
        is_aligned = secuencia_alineada(file)

    fasta_sequences = SeqIO.parse(open(path, 'r'), 'fasta')
    seq_dict = {rec.id : rec.seq for rec in fasta_sequences}
    for x, y in seq_dict.items():
        seqobj = re.search(r'gi.(\d*).gb.(\w*.\d*)',x)
        if seqobj is None:
            error_message = 'El header de ' + x + ' no cumple con el formato fasta requerido.'
            done = False
            break
        if y == '':
            error_message = 'El header ' + x + ' no contiene secuencia.'
            done = False
            break
        if seqobj.group(1) != '' and seqobj.group(2) != '' and x.count("|") == 4:
            print('')
            if not validate(str(y)):
                error_message = 'El contenido de la secuencia no es ADN'
                done = False
                break
            else:
                # alineamiento
                if is_aligned:
                    print(seqobj.group(1))
                    # print(seqobj.group(2))
        else:
            done = False
            break

    fasta_sequences = SeqIO.parse(open(path, 'r'), 'fasta')
    if done:
        for fasta in fasta_sequences:
            fasta_to_insert = Secuence()
            fasta_to_insert.bio_id = fasta.id
            fasta_to_insert.content = fasta.seq
            fasta_to_insert.length = len(fasta.seq)
            fasta_to_insert.save()

        clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile=path)
        assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()
        alignment = AlignIO.read('secuences/secuence.aln', "clustal")
        print(alignment)


        messages.success(request, f"El archivo se ha subido correctamente")
        return render(request, "TpFinalBioApp/uploaded_secuence.html", {'fasta_sequences': fasta_sequences})
    else:
        messages.error(request, f"El archivo no es correcto. " + error_message)
        return redirect('Home')
        

def validate(seq, alphabet='dna'):
    """
    Check that a sequence only contains values from an alphabet

    >>> seq1 = 'acgatGAGGCATTtagcgatgcgatc'       # True for dna and protein
    >>> seq2 = 'FGFAGGAGFGAFFF'                   # False for dna, True for protein
    >>> seq3 = 'acacac '                          # should return False (a space is not a nucleotide)
    >>> validate(seq1, 'dna')
    True
    >>> validate(seq2, 'dna')
    False
    >>> validate(seq2, 'protein')
    True
    >>> validate(seq3, 'dna')
    False

    """
    alphabets = {'dna': re.compile('^[acgtn]*$', re.I),
             'protein': re.compile('^[acdefghiklmnpqrstvwy]*$', re.I)}


    if alphabets[alphabet].search(seq) is not None:
         return True
    else:
         return False

def convertDirectionToCoordinates(self, direction):
    apikey = 'AIzaSyAqJwGQtaGHY5Bm56dMzfcRgRRQ9uCn8G8'
    return gmplot.GoogleMapPlotter.geocode(direction, apikey=apikey)