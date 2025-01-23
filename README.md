# Guide d'installation pour l'API

Ce guide explique comment installer et exécuter le projet d'API.

## Prérequis

1. **Python 3.8 ou version supérieure** : Assurez-vous que Python est installé sur votre système.

   - Vous pouvez vérifier votre version avec la commande :
     ```bash
     python --version
     ```
   - Si Python n'est pas installé, téléchargez-le depuis [python.org](https://www.python.org/downloads/).

2. **pip** : L'outil de gestion des packages Python est nécessaire pour installer les dépendances.

   - Vous pouvez vérifier sa présence avec :
     ```bash
     pip --version
     ```
   - Si pip n'est pas installé, référez-vous à [ce guide](https://pip.pypa.io/en/stable/installation/).

## Instructions d'installation

1. **Clonez le projet** : Clonez le dépôt dans votre environnement local.

   ```bash
   git clone https://github.com/cpe-falafel/IA-FalAPI.git
   ```

2. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Vérifiez l'installation** :

   - Assurez-vous que les packages requis sont correctement installés :
     ```bash
     pip list
     ```

## Lancer le projet

1. Exécutez le fichier `main.py` :

   ```bash
   cd app
   python main.py
   ```

2. L'API devrait maintenant être accessible.

   ```
   http://127.0.0.1:5000
   ```
