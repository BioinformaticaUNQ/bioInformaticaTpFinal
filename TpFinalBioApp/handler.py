import re

from Bio import SeqIO, Entrez

from TpFinalBio.settings.base import BASE_DIR


def handle_uploaded_file(f):
    with open(BASE_DIR +"/secuences/secuence.fasta", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class SequenceHandler():

    is_aligned = False
    _error_message = ''
    _has_errors = False
    _dic_data = []

    def validate_sequences(self, path):

        file = open(path, 'r')

        if not file.readlines()[0].startswith('>'):
            self._error_message = 'la primera linea del archivo no inicia como un fasta >'
            self._has_errors = True
        else:
            self.is_aligned = self.secuencia_alineada(file)

        fasta_sequences = SeqIO.parse(open(path, 'r'), 'fasta')
        seq_dict = {rec.description : rec.seq for rec in fasta_sequences}
        for x, y in seq_dict.items():
            seqobj = re.search(r'gi.(\d*).gb.(\w*.\d*).loc.(.*)', x)
            if seqobj is None:
                self._error_message = 'El header de ' + x + ' no cumple con el formato fasta requerido.'
                self._has_errors = True
                break
            if y == '':
                self._error_message = 'El header ' + x + ' no contiene secuencia.'
                self._has_errors = True
                break
            if seqobj.group(1) != '' and seqobj.group(2) and seqobj.group(3) and x.count("|") == 5:
                
                if not self.validate(str(y)):
                    self._error_message = 'El contenido de la secuencia no es ADN' + 'sec: ' + x
                    self._has_errors = True
                    break
                else:
                    # Busqueda de Accesionns en GenBank
                    Entrez.email = "12345BioInf@ejemplo.com"
                    handle = Entrez.efetch(db="nucleotide", id=seqobj.group(2), rettype="gb", retmode="xml")
                    record = Entrez.read(handle)
                    # loc= (record[0]['GBSeq_references'][1]['GBReference_journal'])
                    # if not 'Submitted' in loc:
                    #     loc= (record[0]['GBSeq_references'][2]['GBReference_journal'])
                    #
                    handle.close()
                    # description = (record[0]['GBSeq_source'])
                    # dic = {'gi':seqobj.group(1),'gb': seqobj.group(2),'loc': seqobj.group(3), 'seq': y, 'description': description}
                    dic = {'gi':seqobj.group(1),'gb': seqobj.group(2),'loc': seqobj.group(3), 'seq': y, 'source': record[0]['GBSeq_source'], 'date':record[0]['GBSeq_create-date']}
                    self._dic_data.append(dic)

                    # alineamiento
                    if self.is_aligned:
                        print(seqobj.group(1))
                        # print(seqobj.group(2))
            else:
                self._has_errors = True
                break

    def secuencia_alineada(self, file):
        return True

    def validate(self, seq, alphabet='dna'):
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

    @property
    def has_errors(self):
        return self._has_errors

    @property
    def error_message(self):
        return self._error_message

    @property
    def dic_data(self):
        return self._dic_data

    def clean_data(self):
        self._dic_data.clear()

    def get_image_path(self, upload_id):
        return "../../static/TpFinalBioApp/img/output/myTree"+"_"+str(upload_id)+".png"