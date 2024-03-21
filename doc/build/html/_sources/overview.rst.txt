.. _overview:

Overview
========

Site Web 2.0 - Caractéristiques et Améliorations
------------------------------------------------

Amélioration de l’Architecture Modulaire
----------------------------------------

Nous optimisons notre architecture de site web en transitionnant d'une conception monolithique à une architecture plus modulaire. Nous prévoyons :

* Réorganisation de notre code en plusieurs applications distinctes.
* Déplacement des fichiers HTML dans des dossiers de templates dédiés à chaque application.

Cette restructuration vise à améliorer la flexibilité, la maintenabilité et l'évolutivité de notre code.

Aspects Techniques
------------------

Pour améliorer la modularité, nous diviserons ``oc_lettings_site`` en deux applications distinctes, ``lettings`` et ``profiles``. Les étapes incluent :

* Création de nouvelles applications ``lettings`` et ``profiles``.
* Migration des données existantes vers les nouvelles structures de tables.
* Suppression des tables obsolètes via les migrations Django.
* Réorganisation et mise à jour des templates et des URLs.
* Maintien de la configuration `ROOT_URLCONF` identique.

Réduction de Divers Problèmes sur le Projet
-------------------------------------------

Nous abordons plusieurs problèmes existants :

* Correction des erreurs de linting sans altérer la configuration existante.
* Correction de la pluralisation incorrecte de "adresse" dans la section d'administration.
* Amélioration de la gestion des erreurs 404 et 500 pour offrir une meilleure expérience utilisateur.
* Ajout de docstrings pour améliorer la compréhension et la documentation du code.
* Mise en place de tests unitaires et d'intégration pour garantir la qualité et le bon fonctionnement de l'application.

Surveillance de l’Application et Suivi des Erreurs via Sentry
-------------------------------------------------------------

Nous intégrerons Sentry pour une meilleure surveillance des erreurs et une gestion robuste :

* Installation et configuration de Sentry.
* Insertion de logs appropriés à des endroits stratégiques dans le code.
* Mise à jour de la documentation pour inclure les instructions de configuration de Sentry.

Pipeline CI/CD et le Déploiement
--------------------------------

Le pipeline CI/CD sera composé de :

* Compilation et tests, vérifiant que la couverture des tests est supérieure à 80%.
* Conteneurisation et étiquetage des images pour Docker, suivi du déploiement sur l'hébergeur choisi.
* Vérification que seules les modifications sur la branche master déclenchent la conteneurisation et le déploiement.

Documentation de l’Application
-------------------------------

Une documentation technique complète sera créée pour détailler :

* La structure du projet.
* Les instructions d'installation et de démarrage rapide.
* Les technologies et langages utilisés.
* La structure de la base de données et des modèles de données.
* Les interfaces de programmation.
* Un guide d'utilisation et des cas d'utilisation.
* Les procédures de déploiement et de gestion de l'application.