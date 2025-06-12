# Utilisation d'une image Python 3.8
FROM python:3.8-slim-buster

# Création d'un utilisateur avec des droits limités
RUN useradd -m -s /bin/bash limited_user

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers de dépendances dans le répertoire de travail
COPY requirements.txt requirements.txt

# Installation des dépendances
RUN pip install -r requirements.txt

# Copie des fichiers du code source dans le répertoire de travail
COPY dice.py dice.py

# Attribution des droits de l'utilisateur limité sur le répertoire de travail
RUN chown -R limited_user:limited_user /app

# Exposition du port 5000
EXPOSE 5000

# Commande pour démarrer l'application en tant qu'utilisateur limité
USER limited_user
CMD ["python", "dice.py"]