# -*- coding: utf-8 -*-

from Bio import Entrez
from Bio import Medline
import urllib

def getMeSH(url):
        query = urllib.unquote_plus(url)

        if not query:
                return "<h3> No query </h3>"
        
        MAX_COUNT = 10000
         
        Entrez.email = 'A.N.Other@example.com'
        pubmedquery = query.replace('-','\-')
        h = Entrez.esearch(db='pubmed', term=pubmedquery, retmax=MAX_COUNT)
        result = Entrez.read(h)
        ids = result['IdList']
        if not ids:
                return "<h3> geen gevonden resultaten </h3>"
        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)

        MeSHCount = 0
        MeSHContent = ""
        
        for record in records:
                try:
                        if "tox" in str(record.get("MH")):
                                MeSHContent += "<h4><a href='http://www.ncbi.nlm.nih.gov/pubmed/"+str(record.get("PMID"))+"'>"
                                MeSHContent += "PMID: "+str(record.get("PMID"))+"</a> is analysed on toxicity. </h4> \n"
                except (TypeError):
                        continue;
                
        return MeSHContent
