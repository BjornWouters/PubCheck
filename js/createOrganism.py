import mysql.connector

def createOrganism():
        conn = mysql.connector.connect (host = "127.0.0.1",
                                        user = "bi2_pg5",
                                        password = "blaat1234",
                                        db= "bi2_pg5")
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM organism "
                          "GROUP BY name")

        organismList = cursor.fetchall()

        organism = ""

        for i in range(len(organismList)):
                hyperlink = str(organismList[i][0]).replace(" ", "+")
                organism += "<tr><td width='100%'>"+str(organismList[i][0])+"</td></tr>\n"               

        cursor.close()
        conn.close()

        return organism