Insert1Http = 'https://synbiohub.org/public/igem/BBa_K576005/1'
# Insert2Http =
PlasmidHttp = 'https://synbiohub.org/public/igem/BBa_J61031/1'

sequence = GetSbolSequence(Insert1Http)
CheckInsertForRes(EcoRI, SpeI, sequence)
primerF, primerR, TM = MakePrimers(EcoRI, SpeI, sequence)
AmpSeq = FakePCR(EcoRI, SpeI, sequence)
GelImageShow(AmpSeq)


Plasmid, resistance = GetSbolSequence(PlasmidHttp)
CheckPlasmidForRes(EcoRI, XbaI, Plasmid)
DigestedPlasmid = DigestPlasmid(EcoRI, XbaI, Plasmid)
DigestedInsert = DigestInsert(EcoRI, SpeI, AmpSeq)
Ligate(DigestedPlasmid, DigestedInsert)
