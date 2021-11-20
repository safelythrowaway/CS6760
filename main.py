# This is the Main script for my project

import Bio
import pydna.design
from Bio.Restriction import *
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
import re


from pydna.dseqrecord import Dseqrecord
from pydna import amplify
from pydna import design

import json, xmltodict

with open('iGEM_2019_Plate1_Well10A.xml', 'r') as myfile:
    obj = xmltodict.parse(myfile.read())
print(json.dumps(obj))




# import requests
#
# response = requests.post(
#     'http://synbiohub.org/login',
#     headers={
#         'X-authorization': '<token>',
#         'Accept': 'text/plain'
#     },
#     data={
#         'email': 'josh.jackson@hsc.utah.edu',
#         'password' : 'jjackson',
#         },
# )
#
# print(response.status_code)
# print(response.content)
#
#
# response = requests.get(
#     'http://synbiohub.org/profile',
#     headers={
#     'X-authorization': '<token>',
#     'Accept': 'text/plain'
#     }
# )
#
# print(response.status_code)
# print(response.content)
#
#
# import requests
#
# sequence = requests.get(
#     'BBa_K576005/sbol',
#     headers={
#         'Accept': 'text/plain',
#         'X-authorization': response.raw
#         },
# )

# print(response.status_code)
# print(response.content)


Plasmid = SeqIO.read('LacI_Promotor_Plasmid.fasta', "fasta")
seqOfInterest =SeqRecord(Seq('aattcgcggccgctt'))
Seq(Plasmid)

#########################################################################################################
### primer design section
#########################################################################################################
def CheckPrimerForRes(enzyme1, enzyme2, dnaInsert):
    Sites = [x for x in [enzyme1, enzyme2] if len(x.search(dnaInsert.seq))>0]
    if not Sites:
        print('No interfearing restriction sites found in Sequence')
    else:
        print(f'{Sites} found in Sequence')
    return Sites

def MakePrimers(enzyme1, enzyme2, dnaInsert):
    if len(dnaInsert) > 30:
        dna = pydna.dseqrecord.Dseqrecord(str(dnaInsert.seq))
        primerObj = pydna.design.primer_design(dnaInsert)
        primerF = enzyme1.site + str(primerObj.forward_primer.seq)
        primerR = str(primerObj.forward_primer.seq) + enzyme2.site.reverse_complement
    elif len(dnaInsert) > 17:
        print("Sequence of Interest Length is less than 30 bp and purifying by gel might be difficult")
        primerLen = len(dnaInsert)
        primerF = enzyme1.site+dnaInsert[0:17]
        primerR = dnaInsert[(primerLen-17):primerlen] + enzyme2.site
    else:
        print('Sequence of Interest Length is less than 17bp, the Primers may not work.  '
              'Additionally, purifying by gel may be difficult.')
        primerF = enzyme1.site + dnaInsert.seq[:]
        primerR = dnaInsert.seq[:] + enzyme2.site
    return(primerF, primerR)


def PrimerPCR(primer1, primer2, template):
    pydna.amplify.pcr()

#########################################################################################################



#########################################################################################################
def Digest(enzyme1, enzyme2, inPlasmid): #do not quote the enzyme names.
    cut1 = enzyme1.catalyse(inPlasmid, linear = False)
    if len(cut1)>1:
        print(enzyme1 +' has more than one cutsite in plasmid')
        exit
    cut1 = cut1[0]
    cut2 = enzyme2.catalyse(cut1, linear = True)
    #need to figure out how to pick the correct sequence from the two that come out.
    return cut2


def singleCutSite():

def getOverhang():

def combineSequeces():

def

# % symbol will compare ends and return true if ligation is possible.


matching = [x for x in test if 'aattcgcgg' in x ]
