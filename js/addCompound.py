import mysql.connector
from QueryBuilder import createQuery
<<<<<<< HEAD
returnString = ""

def addCompound(compound_raw):
        compound = compound_raw.replace("'","") 
        if ";" in compound:
            compoundList = compound.split(";")
            for i in range(len(compoundList)):
                toDatabase(compoundList[i])
            return "Succesfully appended: "+returnString
        else:
            toDatabase(compound)
            return "Succesfully appended: "+compound        

def toDatabase(compound):
        global returnString
=======

def addCompound(compound):
        if ";" in compound:
            compoundList = compound.split(";")
            for i in compoundList:
                toDatabase(compoundList[i])
        else:
            toDatabase(compound)

def toDatabase(compound):
>>>>>>> 467898321e93257e946ea6167d75d92bcceefe24
        conn = mysql.connector.connect (host = "127.0.0.1",
                                        user = "bi2_pg5",
                                        password = "blaat1234",
                                        db= "bi2_pg5")
        cursor_org = conn.cursor()

        cursor_org.execute("SELECT organism_id, name FROM organism")        
        
        organismList = cursor_org.fetchall()

        for i in range(len(organismList)):
                cursor_compound_id = conn.cursor()
                cursor = conn.cursor()
                
                cursor_synonyms = conn.cursor()

                cursor_synonyms.execute("SELECT name FROM synonyms "
                               "WHERE organism_id = "+str(organismList[i][0])+"")

                synonymList = cursor_synonyms.fetchall()

                if synonymList:
                        synonyms = " OR " + ' OR '.join(elem[0] for elem in synonymList)
                
                
                cursor_compound_id.execute("SELECT compound_id FROM compound "
                                "ORDER BY organism_id DESC "
                                "LIMIT 1")                

                (compound_id,) = cursor_compound_id.fetchone()
        
                cursor.execute("INSERT INTO compound "
                               "(compound_id, name, organism_id, query) "
                                "VALUES("+str(compound_id+i+1)+", '"+str(compound)+"', "+str(organismList[i][0])+", '("+str(createQuery(str(organismList[i][1]+synonyms)+")", str(compound)))+"')")

                cursor_compound_id.close()
                cursor_synonyms.close()
                cursor.close()

        cursor_org.close()
        conn.commit()
        conn.close()

        returnString += compound + "\n"
