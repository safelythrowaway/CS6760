# This is the Main script for my project

import Bio
from Bio import Restriction
from Bio.Seq import Seq
from Bio import SeqIO

import pydna

Plasmid = SeqIO.read('LacI_Promotor_Plasmid.fasta', "fasta")
Seq(Plasmid)
dir(Plasmid)
test = Restriction.AllEnzymes.search(Plasmid.seq)
TseI = test.get(Restriction.TseI)