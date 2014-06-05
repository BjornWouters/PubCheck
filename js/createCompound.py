import mysql.connector

def createTable():
        conn = mysql.connector.connect (host = "127.0.0.1",
                                        user = "bi2_pg5",
                                        password = "blaat1234",
                                        db= "bi2_pg5")
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM compound "
                          "GROUP BY name")

        compoundList = cursor.fetchall()

        compounds = ""

        for i in range(len(compoundList)):
                hyperlink = str(compoundList[i][0]).replace(" ", "+")
                compounds += "<tr><td width='100%'>"+str(compoundList[i][0])+"</td></tr>\n"               

        cursor.close()
        conn.close()

        return compounds
