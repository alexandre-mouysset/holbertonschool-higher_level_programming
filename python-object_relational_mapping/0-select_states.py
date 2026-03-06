#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments passés au script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Se connecter à la base MySQL sur localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
        )

    cursor = db.cursor()

    # Exécuter la requête pour récupérer tous les états triés par id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        print(row)

    # Fermer la connexion
    cursor.close()
    db.close()
