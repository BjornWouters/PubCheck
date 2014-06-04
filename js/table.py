# -*- coding: utf-8 -*-

from Bio import Entrez
from Bio import Medline

def createTable(query):

        if not query:
                return "<h3> No query </h3>"
        
        MAX_COUNT = 100
         
        Entrez.email = 'A.N.Other@example.com'
        pubmedquery = query.replace('-','\-')
        h = Entrez.esearch(db='pubmed', term=pubmedquery, retmax=MAX_COUNT)
        result = Entrez.read(h)
        ids = result['IdList']
        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)


        tableContent = ""
        
        for record in records:
                try:    
                        tableContent += "<tr><td width='22%'>"+str(record.get("TI"))+"</td>"\
                        "<td width='5%'>"+str(record.get("DP"))+"</td>"\
                        "<td width='5%'>"+str(writers(record.get("FAU")))+"</td>"\
                        "<td width='5%'>"+str(record.get("JT"))+"</td>"\
                        "<td width='5%'>"+str(query)+"</td>"\
                        "<td>"\
                        "<a href='http://www.ncbi.nlm.nih.gov/pubmed/"+str(record.get("PMID"))+"'><img src='PubMed.png' height='75px' width='75px' alt='PubMed' align='right'/></a>"\
                        +str(record.get("AB"))+"</td></tr>"
                except (TypeError):
                        continue;
                
        return tableContent

def writers(writers):
        try:
                if len(writers) <= 3:
                        return writers
                else:
                        return writers[0:3]
        except (TypeError):
                return None;

                        
