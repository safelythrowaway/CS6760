Insert1Http = 'https://synbiohub.org/public/igem/BBa_K576005/1'
PlasmidHttp = 'https://synbiohub.org/public/igem/BBa_J61031/1'

sequence = GetSbolSequence(Insert1Http)
CheckPrimerForRes(EcoRI, SpeI, sequence)
primerF, primerR, TM = MakePrimers(EcoRI, SpeI, sequence)
AmpSeq = FakePCR(EcoRI, SpeI, sequence)
GelImageShow(AmpSeq)


Plasmid = GetSbolSequence(PlasmidHttp)
Digest(EcoRI, SpeI, Plasmid)
