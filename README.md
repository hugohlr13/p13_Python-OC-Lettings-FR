## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Déploiement

Le déploiement de cette application se fait via une intégration et une livraison continues (CI/CD) en utilisant **CircleCI**. Chaque push dans la branche `master` déclenche le pipeline CI/CD qui exécute les tests automatiques et, s'ils réussissent, déploie l'application sur **Heroku**.

##### Configuration Requise :
Pour que le déploiement fonctionne correctement, vous devez :

1. Avoir un compte sur **Heroku** et **CircleCI**.
2. Configurer les variables d'environnement nécessaires dans votre projet CircleCI, comme `SECRET_KEY`, `DOCKERHUB_USERNAME`,`DOCKERHUB_PASSWORD` `HEROKU_API_KEY`, `HEROKU_APP_NAME` etc.
3. S'assurer que le fichier de configuration CI/CD `.circleci/config.yml` est correctement configuré selon les exigences de l'application.

#### Étapes pour le Déploiement :
1. Connectez-vous à **Heroku** et configurez un nouvelle application avec les variables d'environnement comme `SECRET_KEY` et `SENTRY_DSN`. 
2. Dans **CircleCI**, liez votre dépôt GitHub à votre projet CircleCI.
3. Configurez les variables d'environnement dans CircleCI en vous assurant qu'elles correspondent à celles attendues par l'application.
4. Poussez votre code dans la branche `master`.
5. Surveillez le pipeline CI/CD pour vous assurer que les tests passent et que le déploiement s'effectue correctement.
6. Une fois le déploiement réussi, accédez à l'URL fournie par Heroku pour voir l'application en ligne.

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

