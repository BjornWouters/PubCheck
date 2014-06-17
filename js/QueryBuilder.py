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
compounds = []

def createQuery (organism, compound):
    compounds = []
    clause = compoundSynonyms(compounds, compound)
    Statement = builder(organism,clause)
    return Statement

def compoundSynonyms(compounds, compound): # Synonymen voor compounds vinden
    comp_list = chemspipy.find(compound.lower())
    compounds.append(compound.lower())
    for c in comp_list:
        cmpnd = str(c.commonname).lower().replace("b'",'').replace("'","").replace("b\"",'').replace("\"","")
        if cmpnd not in compounds:
            compounds.append(cmpnd)
    return ' OR '.join(compounds)

def builder(organism,clause): # de query samenstellen
    return ''+organism+' AND ('+clause+')'

