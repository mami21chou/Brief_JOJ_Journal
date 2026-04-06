# JOJ News - Journal Officiel des Supporters

## Description du projet

JOJ News est une plateforme web développée avec Django permettant la publication et la consultation d’articles liés aux Jeux Olympiques de la Jeunesse.

L'objectif du projet est de créer un canal officiel de communication où :

- Les administrateurs publient des articles
- Les utilisateurs consultent les articles
- Les utilisateurs connectés peuvent commenter
- Les administrateurs reçoivent une notification email lorsqu’un commentaire est publié

Ce projet est réalisé dans un cadre pédagogique en binôme.

---

## Fonctionnalités principales

### Gestion des utilisateurs

- Inscription utilisateur
- Connexion et déconnexion
- Authentification sécurisée avec Django
- Affichage du nom de l'utilisateur connecté

### Gestion des articles

- Création d’articles via l’interface admin
- Modification et suppression d’articles
- Organisation des articles par catégories
- Affichage liste des articles
- Affichage détail d’un article

### Gestion des commentaires

- Ajout de commentaire par utilisateur connecté
- Modification de son propre commentaire
- Suppression de son propre commentaire
- Affichage des commentaires associés à un article

### Notifications email

- Envoi automatique d’un email à l’administrateur
- Déclenché après la création d’un commentaire
- Vérifiable dans la console en mode développement

### Interface utilisateur

- Interface responsive
- Utilisation de Bootstrap
- Design inspiré des couleurs olympiques
- Navigation simple et intuitive

---

## Technologies utilisées

Backend :

- Python
- Django
- MySQL

Frontend :

- HTML5
- CSS3
- Bootstrap

Outils :

- Git
- GitHub
- Trello(Taches)
- UML (modélisation)
- MySQL Workbench (base de données)

---


---

## Modèles principaux

### Categorie

Permet d’organiser les articles.

Champs :

- nom

---

### Article

Représente un article publié.

Champs :

- titre
- contenu
- image
- statut
- date_creation
- date_publication
- auteur (User)
- categorie (Categorie)

---

### Commentaire

Permet l’interaction des utilisateurs.

Champs :

- message
- date_publication
- auteur (User)
- article (Article)

---

## Installation du projet

### 1. Cloner le projet

git clone url-du-repository

cd nom_repository_clone
---

### 2. Créer un environnement virtuel
- python -m venv .venv

- Linux: source .venv/bin/activate

- Windows : .venv\Scripts\activate

---

### 3. Installer les dépendances

pip install -r requirements.txt


---

### 4. Configurer la base de données

Créer un fichier `.env` à la racine du projet:
- DB_NAME=dbname
- DB_USER=usernamedb
- DB_PASSWORD=motdepasse
- DB_HOST=localhost
- DB_PORT=3306


Configurer dans `settings.py`.

---

### 5. Appliquer les migrations

python manage.py makemigrations

python manage.py migrate


---

### 6. Créer un super utilisateur


python manage.py createsuperuser

---

### 7. Lancer le serveur

python manage.py runserver

Accès :

http://127.0.0.1:8000

http://127.0.0.1:8000/admin


---

## Configuration email (développement)

Dans `settings.py` :


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'joj@gmail.com'

Les emails seront affichés dans le terminal.

---

## Bonnes pratiques utilisées

- Séparation logique backend/frontend
- Utilisation des signals Django
- Respect des permissions utilisateur
- Organisation du code en applications
- Versionning avec Git
- Planificaion des taches avec Trello
- Utilisation des migrations Django

---

## Sécurité appliquée

- Authentification obligatoire pour commenter
- Un utilisateur ne peut modifier que ses propres commentaires
- Vérification des permissions avant suppression
- Protection CSRF dans les formulaires

---

## Améliorations possibles

- Pagination des articles
- Recherche d’articles
- Filtrage par catégorie
- Upload multiple d’images
- Notifications en base de données
- Ajoustement du design plus propre

---

## Équipe

Projet réalisé en binôme.

Développeurs :

- Aliou DIALLO
- Adji Aissatou Wade SAMBE

---

## Objectifs pédagogiques

Ce projet permet de pratiquer :

- Django MVC (MVT)
- Authentification Django
- Gestion des relations entre modèles
- Envoi d’emails automatiques
- Travail collaboratif avec Git ou Trello pour planification des taches
- Conception UML
- Développement web fullstack

---
