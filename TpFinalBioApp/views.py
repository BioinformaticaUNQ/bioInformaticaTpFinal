import calendar
import json
import os
import re
import platform
import subprocess
import time

from django.core import serializers
from subprocess import Popen, PIPE


import gmplot
from Bio import SeqIO, AlignIO
from Bio.Align.Applications import ClustalwCommandline
from django.contrib import messages
from django.shortcuts import render, redirect
from ete3 import Tree, PhyloTree

from TpFinalBioApp.forms import SecuenceForm
# Create your views here.
from TpFinalBioApp.handler import handle_uploaded_file, SequenceHandler
from TpFinalBioApp.models import Secuence


def home(request):
    return render(request,"TpFinalBioApp/home.html")

def map(request, upload_id):
    data = serializers.serialize('json', Secuence.objects.filter(upload_id = upload_id), fields=('latitud','longitud','bio_id','address'))
    json_dict = json.loads(data)
    return render(request,"TpFinalBioApp/map.html",{'markers': data, 'dataTable': json_dict})

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
    path = 'secuences/secuence.fasta'

    handler = SequenceHandler()
    handler.validate_sequences(path)

    upload_id = calendar.timegm(time.gmtime())

    if not handler.has_errors:
        for fasta in handler.dic_data:
            coordenadas = convertDirectionToCoordinates(fasta['loc'])
            fasta_to_insert = Secuence()
            fasta_to_insert.address = fasta['loc']
            fasta_to_insert.latitud = coordenadas[0]
            fasta_to_insert.longitud = coordenadas[1]
            fasta_to_insert.bio_id = fasta['gb']
            fasta_to_insert.content = fasta['seq']
            fasta_to_insert.length = len(fasta['seq'])
            fasta_to_insert.upload_id = upload_id
            fasta_to_insert.save()

        handler.clean_data()
        clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
        # clustalw_exe = r"/usr/bin/clustalw"
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile=path, output='FASTA', outfile= path + '_aln.fasta' )
        assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()
        alignment = AlignIO.read('secuences/secuence.fasta_aln.fasta', "fasta")
        print('alineamiento \n' + str(alignment))


        cmd = ['powershell.exe', '-ExecutionPolicy', 'ByPass', '-File', 'secuences/scripts/armado del arbol.ps1']
        ec = subprocess.call(cmd)
        #print("Powershell returned: {0:d}".format(ec))
        # os.system('./secuences/scripts/armado del arbol.sh')

        messages.success(request, f"El archivo se ha subido correctamente")
        print(platform.system())
        log_file = open('secuences/secuence.fasta_aln.fasta.log', 'r')
        log_tree = log_file.read().splitlines(False)

        t = PhyloTree("secuences/secuence.fasta_aln.fasta.treefile")
        t.link_to_alignment('secuences/secuence.fasta_aln.fasta')
        t.render("TpFinalBioApp/static/TpFinalBioApp/img/myTree.png", w=300, units="mm")
        print(t)
        os.remove("secuences/secuence.fasta_aln.fasta.model.gz")

        return redirect('Map', upload_id)
    else:
        messages.error(request, f"El archivo no es correcto. " + handler.error_message)
        return redirect('Home')


def convertDirectionToCoordinates(direction):
    apikey = 'AIzaSyAqJwGQtaGHY5Bm56dMzfcRgRRQ9uCn8G8'
    return gmplot.GoogleMapPlotter.geocode(direction, apikey=apikey)