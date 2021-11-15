# This is the Main script for my project

import Bio
from Bio.Restriction import *
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
import re
import pydna
import requests


# This section is for aquiring inputs.  I haven't been able to make this work yet, Talk to Cory about it.

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
#
# print(response.status_code)
# print(response.content)


Plasmid = SeqIO.read('LacI_Promotor_Plasmid.fasta', "fasta")
seqOfInterest =SeqRecord(Seq('aattcgcggccgctt'))

# This function is for checking the registry part for restriction sites EcoRI, SpeI, XbaI

def CheckForSites(enzyme1, enzyme2, enzyme3, seq):
    zymes=[enzyme1.site, enzyme2.site, enzyme3.site]
    matches = [x in seq for x in zymes]
        return matches







# test = Restriction.AllEnzymes.search(Plasmid.seq)
# test = RestrictionBatch([EcoRI, XbaI]).search(Plasmid.seq)
# test = Analysis(RestrictionBatch([EcoRI, XbaI]),Plasmid.seq, linear=False)
# test.print_as('number')
# test.print_that()
#
# test = RestrictionBatch([EcoRI, XbaI]).catalyze(Plasmid.seq)

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
