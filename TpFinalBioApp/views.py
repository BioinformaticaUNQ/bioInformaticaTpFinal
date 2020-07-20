import calendar
import json
import os
import platform
import subprocess
import time

import gmplot
from Bio.Align.Applications import ClustalwCommandline
from django.conf import settings
from django.contrib import messages
from django.core import serializers
from django.shortcuts import render, redirect
from ete3 import PhyloTree, TreeStyle

from TpFinalBio.settings.base import IQTREE_PATH, BASE_DIR
from TpFinalBioApp.forms import SecuenceForm
from TpFinalBioApp.handler import handle_uploaded_file, SequenceHandler
from TpFinalBioApp.models import Secuence


def home(request):
    return render(request,"TpFinalBioApp/home.html")

def map(request, upload_id):
    handler = SequenceHandler()
    log_file = open(BASE_DIR + '/secuences/secuence.fasta_aln.fasta.log', 'r')
    log_tree = log_file.read().splitlines(False)
    log_file.close()
    img = handler.get_image_path(upload_id)
    data = serializers.serialize('json', Secuence.objects.filter(upload_id = upload_id), fields=('latitud','longitud','bio_id','address','source','date'))
    json_dict = json.loads(data)
    return render(request,"TpFinalBioApp/map.html",{'markers': data, 'dataTable': json_dict, 'log': log_tree, 'img': img})

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
    path = BASE_DIR + '/secuences/secuence.fasta'

    handler = SequenceHandler()
    handler.validate_sequences(path)

    upload_id = calendar.timegm(time.gmtime())

    if not handler.has_errors:
        for fasta in handler.dic_data:
            coordenadas = convertDirectionToCoordinates(fasta['loc'])
            fasta_to_insert = Secuence()
            fasta_to_insert.address = fasta['loc']
            fasta_to_insert.date = fasta['date']
            fasta_to_insert.latitud = coordenadas[0]
            fasta_to_insert.longitud = coordenadas[1]
            fasta_to_insert.bio_id = fasta['gb']
            fasta_to_insert.content = fasta['seq']
            fasta_to_insert.length = len(fasta['seq'])
            fasta_to_insert.upload_id = upload_id
            fasta_to_insert.source = fasta['source']
            fasta_to_insert.save()

        handler.clean_data()

        if not handler.is_aligned:
            if platform.system() == 'Linux':
                clustalw_exe = settings.CLUSTAL_PATH
                clustalw_cline = ClustalwCommandline(clustalw_exe, infile=path, output='FASTA', outfile= path + '_aln.fasta' )
                assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
                stdout, stderr = clustalw_cline()

                f = open(BASE_DIR + '/secuences/scripts/scriptarbol.sh', 'w')
                f.write(
                    IQTREE_PATH  + " -s "  + BASE_DIR + "/secuences/secuence.fasta_aln.fasta" + " -m MFP -bb 1000 -redo")
                f.close()
                os.system(BASE_DIR + '/secuences/scripts/scriptarbol.sh')
            else:

                handler.win_alignment(path)

                handler.win_build_tree()
        else:
            # la secuencia esta alineada
            handler.make_file_aln_for_iqtree()
            handler.win_build_tree()
            print("flujo de secuencia alineada")


        messages.success(request, f"El archivo se ha subido correctamente")
        tree_file = BASE_DIR + "/secuences/secuence.fasta_aln.fasta.treefile"
        aln_path = BASE_DIR +"/secuences/secuence.fasta_aln.fasta"

        ts = TreeStyle()
        ts.force_topology = True
        ts.show_leaf_name = False
        ts.branch_vertical_margin = 10

        t = PhyloTree(tree_file)
        t.link_to_alignment(aln_path)
        img_name = "TpFinalBioApp/static/TpFinalBioApp/img/output/myTree"+"_"+str(upload_id)+".svg"
        t.render(img_name, tree_style=ts)
        print(t)
        if platform.system() != 'Linux': os.remove(BASE_DIR + "/secuences/secuence.fasta_aln.fasta.model.gz")

        return redirect('Map', upload_id)
    else:
        messages.error(request, f"El archivo no es correcto. " + handler.error_message)
        return redirect('Home')


def convertDirectionToCoordinates(direction):
    apikey = settings.GOOGLE_MAPS_API_KEY
    return gmplot.GoogleMapPlotter.geocode(direction, apikey=apikey)