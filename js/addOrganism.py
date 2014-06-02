import mysql.connector
from QueryBuilder import createQuery

def appendDatabase(organism):
        conn = mysql.connector.connect (host = "127.0.0.1",
                                        user = "bi2_pg5",
                                        password = "blaat1234",
                                        db= "bi2_pg5")
        cursor = conn.cursor()
        cursor_id = conn.cursor()
        cursor_com = conn.cursor()


        cursor_id.execute("SELECT organism_id FROM organism "
                          "ORDER BY organism_id DESC "
                          "LIMIT 1")

        (organism_id,) = cursor_id.fetchone()

        add_organism =   "INSERT INTO organism "\
                         "(organism_id, name) "\
                         "VALUES ("+str(organism_id+1)+", '"+organism+"')"
        
        cursor.execute(add_organism)

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
                                "VALUES ("+str(compound_id+1)+", '"+str(compoundList[i][1])+"', "+str(organism_id+1)+", '"+str(createQuery(organism, str(compoundList[i][1])))+"')"
                cursor_org.execute(add_organism)
                cursor_org_id.close()
                cursor_org.close()                

        cursor.close()
        cursor_id.close()
        cursor_com.close()
        conn.commit()
        conn.close()

        return "Succesfully appended: "+organism
