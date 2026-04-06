# Resume de revision - Fonctions utilisees

## Python

### 1) Bases (affichage, conversions, iteration)
| Fonction | Utilite | Syntaxe simple |
|---|---|---|
| print() | Afficher une valeur dans le terminal | print("Bonjour") |
| len() | Obtenir la taille d'une sequence | len(ma_liste) |
| range() | Generer une suite d'entiers pour les boucles | range(0, 10, 1) |
| int() | Convertir en entier | int("42") |
| float() | Convertir en decimal | float("3.14") |
| str() | Convertir en chaine | str(42) |
| ord() | Code ASCII/Unicode d'un caractere | ord("A") |
| chr() | Caractere depuis un code | chr(65) |
| isinstance() | Verifier le type d'un objet | isinstance(x, int) |
| type() | Recuperer le type exact | type(x) |
| sorted() | Retourner une version triee | sorted(ma_liste) |
| list() | Convertir vers liste | list(mon_iterable) |
| tuple() | Convertir vers tuple | tuple(ma_liste) |
| map() | Appliquer une fonction a chaque element | map(f, ma_liste) |
| sum() | Somme des elements numeriques | sum(ma_liste) |
| round() | Arrondir un nombre | round(3.14159, 2) |

### 2) Listes, dictionnaires et chaines
| Fonction / methode | Utilite | Syntaxe simple |
|---|---|---|
| append() | Ajouter un element en fin de liste | ma_liste.append(x) |
| extend() | Ajouter plusieurs elements | ma_liste.extend([1, 2]) |
| pop() | Retirer (et retourner) un element | ma_liste.pop() |
| remove() | Supprimer une valeur precise | ma_liste.remove(x) |
| copy() | Copier une liste/dict | copie = ma_liste.copy() |
| get() | Lire une valeur de dict sans erreur | mon_dict.get("cle") |
| keys() | Recuperer les cles d'un dict | mon_dict.keys() |
| items() | Recuperer paires cle/valeur | mon_dict.items() |
| replace() | Remplacer du texte dans une chaine | texte.replace("a", "b") |
| join() | Joindre une liste de chaines | ", ".join(mots) |
| format() | Formater une chaine | "{} {}".format(a, b) |

### 3) Exceptions et tests
| Fonction / classe | Utilite | Syntaxe simple |
|---|---|---|
| TypeError | Signaler un mauvais type | raise TypeError("message") |
| ValueError | Signaler une valeur invalide | raise ValueError("message") |
| Exception | Erreur generique | raise Exception("message") |
| assertEqual() | Verifier un resultat en test unitaire | self.assertEqual(attendu, obtenu) |

### 4) Fichiers, JSON, CSV, XML, pickle
| Fonction | Utilite | Syntaxe simple |
|---|---|---|
| open() | Ouvrir un fichier | open("fichier.txt", "r") |
| read() | Lire le contenu d'un fichier | f.read() |
| write() | Ecrire dans un fichier | f.write("texte") |
| close() | Fermer un fichier | f.close() |
| json.dumps() | Objet Python -> texte JSON | json.dumps(data) |
| json.dump() | Objet Python -> fichier JSON | json.dump(data, f) |
| json.loads() | Texte JSON -> objet Python | json.loads(s) |
| json.load() | Fichier JSON -> objet Python | json.load(f) |
| csv.DictReader() | Lire un CSV en dictionnaires | csv.DictReader(f) |
| writeheader() | Ecrire l'entete CSV | writer.writeheader() |
| writerows() | Ecrire plusieurs lignes CSV | writer.writerows(lignes) |
| pickle.dump() | Serialiser un objet binaire | pickle.dump(obj, f) |
| pickle.load() | Deserialiser un objet binaire | pickle.load(f) |
| ET.parse() | Lire un fichier XML | ET.parse("data.xml") |
| getroot() | Recuperer la racine XML | tree.getroot() |

### 5) POO (classes et methodes speciales)
| Fonction / methode | Utilite | Syntaxe simple |
|---|---|---|
| __init__() | Initialiser un objet | def __init__(self, ...): |
| __str__() | Affichage lisible de l'objet | def __str__(self): |
| __repr__() | Representation technique de l'objet | def __repr__(self): |
| __del__() | Action a la suppression de l'objet | def __del__(self): |
| __next__() | Iterateur (prochain element) | def __next__(self): |
| super() | Appeler la classe parente | super().__init__(...) |
| vars() | Dictionnaire des attributs d'un objet | vars(obj) |

### 6) Bases de donnees (MySQL + SQLAlchemy)
| Fonction / methode | Utilite | Syntaxe simple |
|---|---|---|
| MySQLdb.connect() | Ouvrir une connexion MySQL | MySQLdb.connect(host=..., user=...) |
| cursor() | Creer un curseur SQL | conn.cursor() |
| execute() | Executer une requete SQL | cursor.execute("SELECT ...") |
| fetchall() | Recuperer tous les resultats | cursor.fetchall() |
| create_engine() | Creer un moteur SQLAlchemy | create_engine("mysql+mysqldb://...") |
| sessionmaker() | Fabrique de sessions SQLAlchemy | Session = sessionmaker(bind=engine) |
| query() | Construire une requete ORM | session.query(State) |
| filter() | Ajouter un filtre | query.filter(State.name == "A") |
| order_by() | Trier le resultat | query.order_by(State.id) |
| first() | Recuperer le premier resultat | query.first() |
| all() | Recuperer tous les resultats | query.all() |
| add() | Ajouter un objet a inserer | session.add(obj) |
| commit() | Valider les changements | session.commit() |

### 7) Web/API (Flask, requests, auth)
| Fonction / decorateur | Utilite | Syntaxe simple |
|---|---|---|
| Flask() | Creer l'application web | app = Flask(__name__) |
| route() | Definir une route HTTP | @app.route("/status") |
| jsonify() | Retourner du JSON propre | return jsonify(data) |
| render_template() | Rendre une page HTML | render_template("index.html") |
| request.get_json() | Lire JSON envoye par le client | request.get_json() |
| run() | Lancer le serveur Flask | app.run(host="0.0.0.0", port=5000) |
| requests.get() | Appel HTTP GET | requests.get(url) |
| response.json() | JSON de la reponse HTTP | response.json() |
| generate_password_hash() | Hacher un mot de passe | generate_password_hash(password) |
| check_password_hash() | Verifier un mot de passe | check_password_hash(hash, password) |
| jwt_required() | Proteger une route avec JWT | @jwt_required() |
| get_jwt() | Lire claims JWT courants | get_jwt() |

## JavaScript

### 1) Bases (console, arguments, nombres)
| Fonction / methode | Utilite | Syntaxe simple |
|---|---|---|
| console.log() | Afficher dans la console | console.log("Hello") |
| parseInt() | Convertir chaine -> entier | parseInt("42", 10) |
| isNaN() | Verifier si valeur non numerique | isNaN(x) |
| slice() | Extraire une partie d'un tableau/chaine | args.slice(2) |
| map() | Transformer un tableau | arr.map(x => x + 1) |

### 2) DOM (manipulation HTML)
| Fonction / methode | Utilite | Syntaxe simple |
|---|---|---|
| document.querySelector() | Selectionner un element HTML | document.querySelector("#id") |
| addEventListener() | Ecouter un evenement | el.addEventListener("click", fn) |
| classList.add() | Ajouter une classe CSS | el.classList.add("red") |
| classList.contains() | Verifier presence d'une classe | el.classList.contains("red") |
| classList.replace() | Remplacer une classe par une autre | el.classList.replace("red", "green") |
| document.createElement() | Creer un nouvel element HTML | document.createElement("li") |
| appendChild() | Ajouter un enfant dans le DOM | ul.appendChild(li) |

### 3) API HTTP (asynchrone)
| Fonction / methode | Utilite | Syntaxe simple |
|---|---|---|
| fetch() | Requete HTTP | const response = await fetch(url) |
| response.json() | Lire le JSON de la reponse | const data = await response.json() |
| then() | Chainer des promesses | fetch(url).then(r => r.json()) |

## SQL

### 1) Fonctions SQL reelles utilisees
| Fonction | Utilite | Syntaxe simple |
|---|---|---|
| COUNT() | Compter des lignes | SELECT COUNT(*) FROM table; |
| AVG() | Calculer une moyenne | SELECT AVG(score) FROM table; |

### 2) Requetes principales (tres utilisees dans tes fichiers)
| Commande | Utilite | Syntaxe simple |
|---|---|---|
| SHOW DATABASES | Lister les bases | SHOW DATABASES; |
| SHOW TABLES | Lister les tables | SHOW TABLES; |
| SHOW CREATE TABLE | Voir le SQL de creation d'une table | SHOW CREATE TABLE ma_table; |
| SHOW GRANTS | Voir les privileges d'un user | SHOW GRANTS FOR 'user'@'localhost'; |
| CREATE DATABASE | Creer une base | CREATE DATABASE IF NOT EXISTS db; |
| DROP DATABASE | Supprimer une base | DROP DATABASE IF EXISTS db; |
| CREATE TABLE | Creer une table | CREATE TABLE nom (...); |
| CREATE USER | Creer un utilisateur SQL | CREATE USER 'u'@'localhost' IDENTIFIED BY 'pwd'; |
| GRANT | Donner des droits | GRANT SELECT ON db.* TO 'u'@'localhost'; |
| INSERT INTO | Inserer des lignes | INSERT INTO table(col1) VALUES(val1); |
| SELECT | Lire des donnees | SELECT col FROM table; |
| UPDATE | Modifier des donnees | UPDATE table SET col = val WHERE ...; |
| DELETE | Supprimer des lignes | DELETE FROM table WHERE ...; |

### 3) Filtres, tri, jointures
| Element | Utilite | Syntaxe simple |
|---|---|---|
| WHERE | Filtrer des lignes | SELECT * FROM t WHERE id = 1; |
| ORDER BY | Trier des resultats | SELECT * FROM t ORDER BY score DESC; |
| GROUP BY | Regrouper pour agregats | SELECT score, COUNT(*) FROM t GROUP BY score; |
| INNER JOIN | Associer lignes correspondantes | SELECT ... FROM a INNER JOIN b ON ...; |
| LEFT JOIN | Garder toutes les lignes de gauche | SELECT ... FROM a LEFT JOIN b ON ...; |
| Sous-requete | Requete dans une requete | WHERE id = (SELECT id FROM ...); |

### 4) Contraintes SQL que tu as utilisees
| Contrainte | Utilite | Syntaxe simple |
|---|---|---|
| PRIMARY KEY | Cle principale unique | id INT AUTO_INCREMENT PRIMARY KEY |
| FOREIGN KEY | Lien entre tables | FOREIGN KEY (state_id) REFERENCES states(id) |
| NOT NULL | Valeur obligatoire | name VARCHAR(256) NOT NULL |
| UNIQUE | Interdire les doublons | id INT UNIQUE |
| DEFAULT | Valeur par defaut | id INT DEFAULT 1 |
| AUTO_INCREMENT | Incrementation automatique | id INT AUTO_INCREMENT |

---
