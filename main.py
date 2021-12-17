# This is the main script for my project

import Bio
import pydna.design
from Bio.Restriction import *
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from pydna.gel import gel
from pydna.ladders import PennStateLadder
from pydna.dseqrecord import Dseqrecord
from pydna import amplify
from pydna import design
import re
import requests
from PIL import Image
from pydna.gel import gel
from pydna.ladders import PennStateLadder
from Bio.SeqUtils import MeltingTemp as mt
import pandas as pd



##############################################################################################################
## Get sequences from synbiohub

def GetSbolSequence(https):
    response = requests.get(
    str(https+'/sbol'),
    headers={
        'Accept': 'text/plain',
        'X-authorization': '<token>'
        },
    )
    sequence = Seq(re.findall(r'elements>(.*)</sbol:elements>', str(response.text))[0])
    resistance = re.findall(r'\ (\w*)\ resistance', str(response.text), re.IGNORECASE)
    if bool(resistance):
        return sequence, resistance
    else:
        return sequence

#########################################################################################################
### primer design section

def CheckInsertForRes(enzyme1, enzyme2, dnaInsert):
    Sites = [x for x in [enzyme1, enzyme2] if len(x.search(dnaInsert))>0]
    if not Sites:
        print('No interfearing restriction sites found in Sequence')
    else:
        print(f'{Sites} found in Sequence')
    return Sites

def MakePrimers(enzyme1, enzyme2, dnaInsert):
    if len(dnaInsert) > 30:
        dna = pydna.dseqrecord.Dseqrecord(str(dnaInsert))
        primerObj = pydna.design.primer_design(dna)
        primerF = enzyme1.site + str(primerObj.forward_primer.seq)
        primerR = str(Seq(str(primerObj.reverse_primer.seq) + str(Seq(enzyme2.site).reverse_complement())))
        TMF = mt.Tm_NN(primerF)
        TMR = mt.Tm_NN(primerR)
        TM = min(TMR, TMF)
    elif len(dnaInsert) > 17:
        print("Sequence of Interest Length is less than 30 bp and purifying by gel might be difficult")
        primerLen = len(dnaInsert)
        primerF = enzyme1.site+dnaInsert[0:17]
        primerR = str(Seq(dnaInsert[(primerLen-17):primerlen] + enzyme2.site).reverse_complement())
        TMF = mt.Tm_NN(primerF)
        TMR = mt.Tm_NN(primerR)
        TM = min(TMR, TMF)
    else:
        print('Sequence of Interest Length is less than 17bp, the Primers may not work.  '
              'Additionally, purifying by gel may be difficult.')
        primerF = enzyme1.site + dnaInsert[:]
        primerR = str(Seq(dnaInsert.seq[:] + enzyme2.site).reverse_complement())
        TMF = mt.Tm_NN(primerF)
        TMR = mt.Tm_NN(primerR)
        TM = min(TMR, TMF)
    return(primerF, primerR, TM)


def InsertPCR(primer1, primer2, template):
    pydna.amplify.pcr(primer1, primer2, template)


def FakePCR(enzyme1, enzyme2, template):
    completeSeq= enzyme1.site + template + Seq(enzyme2.site).reverse_complement()
    return (completeSeq)

#########################################################################################################
## Visualize Products

def GelImageShow(target):
    gel([PennStateLadder, [Dseqrecord(target)]]).show()

#########################################################################################################
##Check Plasmid for Restriction sites.
def CheckPlasmidForRes(enzyme1, enzyme2, dnaInsert):
    Sites = [x for x in [enzyme1, enzyme2] if len(x.search(dnaInsert))>0]
    if not Sites:
        print('Restriction sites not found in Sequence')
    else:
        print(f'{Sites} found in Sequence')
    return Sites

########################################################################################################
##Assemble with Plasmid

def DigestPlasmid(enzyme1, enzyme2, inPlasmid): #do not quote the enzyme names.
    cut1 = Dseqrecord(inPlasmid, circular=True).cut(enzyme1)
    if len(cut1)>1:
        print(enzyme1 +' has more than one cutsite in plasmid')
        exit
    cut1 = cut1[0]
    cut2 = cut1.cut(enzyme2)
    lenCheck = []
    for seq in cut2:
        x = seq.seq
        lenCheck.append(x)
    cut3 = max(lenCheck, key=len)
    return cut3

def DigestInsert(enzyme1, enzyme2, Insert):
    DInsert = Dseqrecord(Insert)
    DInsert = max(DInsert.cut(EcoRI, SpeI), key=len)
    return DInsert.seq

def Ligate(PlasmidDigest, InsertDigest):
    Cassette = (PlasmidDigest+InsertDigest).looped()
    return Cassette

def FirstExpressionVectorOutput(Insert1Http, PlasmidHttP):
    sequence = GetSbolSequence(Insert1Http)
    CheckInsertForRes(EcoRI, SpeI, sequence)
    primerF, primerR, TM = MakePrimers(EcoRI, SpeI, sequence)
    AmpSeq = FakePCR(EcoRI, SpeI, sequence)
    GelImage = GelImageShow(AmpSeq)
    Plasmid, resistance = GetSbolSequence(PlasmidHttp)
    CheckPlasmidForRes(EcoRI, XbaI, Plasmid)
    DigestedPlasmid = DigestPlasmid(EcoRI, XbaI, Plasmid)
    DigestedInsert = DigestInsert(EcoRI, SpeI, AmpSeq)
    ExpressionVector = Ligate(DigestedPlasmid, DigestedInsert)
    data = {'Insert Sequence': [str(sequence)],
            'Forward Primer':[str(primerF)],
            'Reverse Primer':[str(primerR)],
            'Anneal Temp':[str(TM)],
            'Gel Image':[GelImage],
            'Expression Vector Resistance':[str(resistance)],
            'Ligated Sequence':[str(ExpressionVector)]}
    df = pd.DataFrame.from_dict(data)
    df.to_excel('Test.xlsx')