InsertHttp = 'https://synbiohub.org/public/igem/BBa_K576005/1'
PlasmidHttp = 'https://synbiohub.org/public/igem/BBa_J61031/1'

sequence = GetSbolSequence(InsertHttp)
CheckPrimerForRes(EcoRI, SpeI, sequence)
primerF, primerR = MakePrimers(EcoRI, SpeI, sequence)
AmpSeq = FakePCR(primerF, primerR, sequence)
GelImageShow(AmpSeq)


Plasmid = GetSbolSequence(PlasmidHttp)
Digest(EcoRI, SpeI, Plasmid)