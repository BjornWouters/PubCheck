##############################################################################################################
##############################################################################################################
## QueryBuilder.py
## Function:               Builds a query to get synonyms for organism and compound (if any) and gets all info from our database
## 
## Version:                 4.2
##
##
##
##
##
##
##############################################################################################################
##############################################################################################################
#from mod_python import apache
import mysql.connector as con
import chemspipy

def createQuery (organism, compound):
    organisms = []
    compounds = []
    clause1 = synonyms(organisms,organism)
    clause2 = compoundSynonyms(compounds,compound)
    Statement = builder(clause1,clause2)
    return Statement
    
def synonyms(List, Term): # Synonymen voor organismen splitsen
    List = Term.lower().split(", ")
    lijst = ') OR '.join(List)
    return lijst

def compoundSynonyms(compounds,compound): # Synonymen voor compounds vinden
    comp_list = chemspipy.find(compound.lower())
    compounds.append(compound.lower())
    for c in comp_list:
        cmpnd = str(c.commonname).lower().replace("b'",'').replace("'","").replace("b\"",'').replace("\"","")
        if cmpnd not in compounds:
            compounds.append(cmpnd)
    return ') OR '.join(compounds)

def builder(clause1,clause2): # de query samenstellen
    string=''
    for x in organisms:
        string+='('
    for x in compounds:
        string+='('
    return string+clause1+') AND '+clause2

