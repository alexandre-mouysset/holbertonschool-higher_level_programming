
# Cours Semaine 5 – Programmation Orientée Objet (Python)

---

## Pourquoi Python est génial
Python est apprécié car :
- sa syntaxe est simple et lisible
- il permet d’écrire moins de code pour faire plus
- il supporte plusieurs paradigmes (procédural, fonctionnel, OOP)
- **tout est objet**, ce qui rend le langage cohérent

```python
x = 42
print(type(x))  # <class 'int'>
```

Même les entiers sont des objets.

---

## “First-class everything”
En Python, les éléments suivants sont des objets :
- fonctions
- classes
- méthodes
- types

```python
def hello():
    return "Hello"

f = hello
print(f())
```

👉 Une fonction peut être stockée dans une variable.

---

## Programmation Orientée Objet (OOP)
L’OOP permet de représenter le monde réel avec :
- des **objets**
- qui ont des **attributs**
- et des **méthodes**

Objectifs :
- structurer le code
- faciliter la maintenance
- réutiliser le code

---

## Classe
Une classe est un **plan** qui définit le comportement futur des objets.

```python
class Car:
    pass
```

---

## Objet et instance
Un objet est une **instance** d’une classe.

```python
my_car = Car()
```

👉 `Car` est la classe  
👉 `my_car` est l’objet

---

## Différence entre classe et objet
- La classe décrit
- L’objet existe réellement en mémoire

```python
car1 = Car()
car2 = Car()
```

`car1` et `car2` sont deux objets différents.

---

## Attribut
Un attribut est une variable attachée à un objet.

```python
my_car.color = "red"
print(my_car.color)
```

---

## Attributs publics, protégés et privés
Python utilise des **conventions** :

```python
class User:
    def __init__(self):
        self.name = "Tom"       # public
        self._age = 25          # protégé
        self.__password = "123" # privé
```

- `_age` → usage interne
- `__password` → name mangling

---

## self
`self` représente l’objet courant.

```python
class User:
    def greet(self):
        print("Hello")
```

Sans `self`, Python ne sait pas sur quel objet agir.

---

## Méthode
Une méthode est une fonction définie dans une classe.

```python
class Dog:
    def bark(self):
        print("Woof")
```

---

## Méthode spéciale __init__
Appelée automatiquement à la création de l’objet.

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Alice")
```

---

## Abstraction, Encapsulation, Information Hiding

### Data Abstraction
On expose seulement ce qui est utile.

### Data Encapsulation
On regroupe données + logique.

### Information Hiding
On protège les données sensibles.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

---

## Property
Une property permet de contrôler l’accès à un attribut.

```python
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

---

## Attribut vs Property
- Attribut : accès direct
- Property : accès contrôlé

```python
u.age = 30  # passe par le setter
```

---

## Getters et Setters (Pythonic)
Python évite les `get_age()`.

```python
class User:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age invalide")
        self._age = value
```

---

## Attributs dynamiques
Python permet d’ajouter des attributs à la volée.

```python
u.city = "Paris"
print(u.city)
```

---

## Attributs de classe
Partagés par toutes les instances.

```python
class User:
    species = "human"
```

---

## Attribut d’objet vs attribut de classe
```python
u1 = User()
u2 = User()

u1.species = "alien"
```

👉 `u1` a son propre attribut `species`.

---

## Méthode de classe
Agit sur la classe, pas sur l’objet.

```python
class User:
    species = "human"

    @classmethod
    def get_species(cls):
        return cls.species
```

---

## Méthode statique
Fonction utilitaire liée à une classe.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

---

## __str__ et __repr__
```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"User(name={self.name})"
```

---

## Différence __str__ / __repr__
- `__str__` → affichage utilisateur
- `__repr__` → debug / développeur

---

## __dict__
Contient les attributs internes.

```python
u.__dict__
User.__dict__
```

---

## Recherche des attributs
Ordre :
1. instance
2. classe
3. classes parentes

---

## getattr
Accès dynamique aux attributs.

```python
getattr(u, "name")
getattr(u, "age", 0)
```

---

## Conclusion
Tu maîtrises maintenant :
- les fondations de l’OOP
- la philosophie Python
- la gestion interne des objets
- les bonnes pratiques pythonic
