# This is the Main script for my project

import Bio
from Bio.Restriction import *
from Bio.Seq import Seq
from Bio import SeqIO


import pydna

Plasmid = SeqIO.read('LacI_Promotor_Plasmid.fasta', "fasta")
Seq(Plasmid)
dir(Plasmid)
# test = Restriction.AllEnzymes.search(Plasmid.seq)
# test = RestrictionBatch([EcoRI, XbaI]).search(Plasmid.seq)
# test = Analysis(RestrictionBatch([EcoRI, XbaI]),Plasmid.seq, linear=False)
# test.print_as('number')
# test.print_that()
#
# test = RestrictionBatch([EcoRI, XbaI]).catalyze(Plasmid.seq)

def Digest(enzyme1, enzyme2, plasmid): #do not quote the enzyme names.
    cut1 = enzyme1.catalyse(plasmid, linear = False)
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