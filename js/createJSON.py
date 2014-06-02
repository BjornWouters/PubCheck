import mysql.connector

def createJSON(compound):
        conn = mysql.connector.connect (host = "127.0.0.1",
                                        user = "bi2_pg5",
                                        password = "blaat1234",
                                        db= "bi2_pg5")

        cursor = conn.cursor()
        cursor_organism = conn.cursor()

        cursor.execute("SELECT query FROM compound "
                        "WHERE name ='"+compound+"'")

        compoundList = cursor.fetchall()

        cursor_organism.execute("SELECT name FROM organism ")

        organismList = cursor_organism.fetchall()

        JSON = '{"name": "Compound", "children": [ { "name": "'+compound+'",'\
               '"children": [ { "name": "Organism", "children": ['
        
        for i in range(len(compoundList)):
                JSON += '{"name": "'+str(organismList[i][0])+'",'
                JSON += '"children": ['
                JSON += '{"name": "Publications", "size": 0,'
                JSON += '"url": "javascript:generateTable('
                JSON += "'"+str(compoundList[i][0])+"'"
                JSON += ')"},{"name": "Analyse",  "url": "javascript:my_Function()"}]'
                if i == len(compoundList)-1:
                        JSON += '}'
                else:
                        JSON += '},'
        JSON += ']}]}]}'

        cursor.close()
        cursor_organism.close()
        conn.close()

        JSON_file = open("/home/bi2_pg5/public_html/webapplicatie/PubCheck/data/data.json", "w")
        JSON_file.write(JSON)
        JSON_file.flush()
        JSON_file.close()
        
        return JSON
