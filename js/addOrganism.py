import mysql.connector
from QueryBuilder import createQuery

def appendDatabase(organism, synonymList):
        synonyms = ""

        conn = mysql.connector.connect (host = "127.0.0.1",
                                        user = "bi2_pg5",
                                        password = "blaat1234",
                                        db= "bi2_pg5")
        cursor = conn.cursor()
        cursor_id = conn.cursor()
        cursor_com = conn.cursor()
        cursor_syn_id = conn.cursor()

        cursor_id.execute("SELECT organism_id FROM organism "
                          "ORDER BY organism_id DESC "
                          "LIMIT 1")

        (organism_id,) = cursor_id.fetchone()

        add_organism =   "INSERT INTO organism "\
                         "(organism_id, name) "\
                         "VALUES ("+str(organism_id+1)+", '"+organism+"')"
        
        cursor.execute(add_organism)

        if synonymList:
                synonyms += " OR "
                
                cursor_syn_id.execute("SELECT synonym_id FROM synonyms "
                                      "ORDER BY synonym_id DESC "
                                      "LIMIT 1")

                (synonym_id,) = cursor_syn_id.fetchone()
                
                for i in range(len(synonymList)):
                        if i == len(synonymList)-1:
                                synonyms += synonymList[i]
                        else:
                                synonyms += synonymList[i]+" OR "

                        cursor_syn = conn.cursor()

                        cursor_syn.execute("INSERT INTO synonyms "
                                           "(synonym_id, name, organism_id) "
                                           "VALUES ("+str(synonym_id+1+i)+", '"+str(synonymList[i])+"', "+str(organism_id+1)+")")

                        cursor_syn.close()
                

        cursor_com.execute("SELECT compound_id, name FROM compound "
                           "WHERE organism_id=0;")

        compoundList = cursor_com.fetchall()

        for i in range(len(compoundList)):
                cursor_org = conn.cursor()
                cursor_org_id = conn.cursor()
                cursor_org_id.execute("SELECT compound_id FROM compound "
                                "ORDER BY organism_id DESC "
                                "LIMIT 1")

                (compound_id,) = cursor_org_id.fetchone()
                add_organism = "INSERT INTO compound "\
                                "(compound_id, name, organism_id, query) "\
                                "VALUES ("+str(compound_id+1)+", '"+str(compoundList[i][1])+"', "+str(organism_id+1)+", '"+str(createQuery("("+organism+synonyms+")", str(compoundList[i][1])))+"')"
                cursor_org.execute(add_organism)
                cursor_org_id.close()
                cursor_org.close()                

        cursor.close()
        cursor_id.close()
        cursor_com.close()
        cursor_syn_id.close()
        conn.commit()
        conn.close()

        return "Succesfully appended: "+organism
