.. _deployment_management:

Gestion du Déploiement
======================

Le déploiement de cette application Django peut être effectué sur des plateformes cloud telles que Heroku ou AWS. L'application utilise Gunicorn comme serveur WSGI pour servir l'application et Whitenoise pour servir les fichiers statiques. Un pipeline CI/CD a été mis en œuvre via CircleCi, et la conteneurisation est effectuée via Docker Hub & Docker Desktop. Le pipeline est composé de trois étapes :

- **Tests et Linting**
- **Construction et push de l'Image Docker**
- **Déploiement sur Heroku**

Veuillez noter que tout changement appliqué à une branche donnée déclenche uniquement le premier travail (tests et linting). Le workflow complet du test au déploiement n'est déclenché que par des changements appliqués à la branche master, à condition qu'aucune erreur n'ait été soulevée.

Prérequis
---------
- **Créer une application Heroku** : Initialisez une application sur Heroku.
- **Construire une image Docker du projet localement** : Utilisez Docker Desktop pour construire l'image Docker de votre application.
- **Pousser l'image Docker sur Docker Hub** : Téléchargez votre image Docker dans votre dépôt Docker Hub.
- **Créer un projet CircleCI** : Configurez votre projet sur CircleCI pour l'intégration continue.
- **Créer un compte Sentry et mettre à jour la clé DSN dans settings.py** : Inscrivez-vous sur Sentry et configurez-le pour surveiller votre application.

Configuration des Variables d'Environnement
-------------------------------------------
Assurez-vous que les variables d'environnement nécessaires sont définies dans CircleCi avant le déploiement. Celles-ci incluent :

- **SSH Keys** : configurez votre clé publique dans votre projet CircleCi et GitHub.
- **DOCKERHUB_USERNAME** : Votre nom d'utilisateur Docker Hub.
- **DOCKERHUB_PASSWORD** : Votre mot de passe Docker Hub.
- **HEROKU_API_KEY** : Votre jeton d'authentification Heroku.
- **HEROKU_APP_NAME** : Le nom de votre application Heroku.

Surveillance et Alerte
----------------------
La mise en place d'un système de surveillance et d'alerte pour les applications en production est cruciale. Implémentez des outils comme Sentry pour le suivi et l'alerte sur les erreurs. Cela garantit que tout problème peut être rapidement identifié et résolu, maintenant ainsi la stabilité et la fiabilité de l'application.
