.. _database_structure:

Structure de la base de données et des modèles de données
=========================================================

Cette section décrit la configuration de la base de données et la structure des modèles de données utilisés dans le projet. Le projet utilise SQLite à des fins de développement en raison de sa simplicité et de sa facilité de configuration. Le schéma de la base de données comprend deux modèles principaux : Letting et Profile.

Modèle Letting
--------------
Le modèle Letting est conçu pour représenter des annonces de location. Chaque annonce comprend les champs suivants :

- Name : Un titre descriptif pour l'annonce de location.
- Address : L'adresse physique du bien à louer.

Ce modèle permet à l'application de stocker et de gérer des informations sur diverses annonces de location disponibles pour les utilisateurs.

Modèle Profile
--------------
Le modèle Profile représente les utilisateurs de l'application. Il comprend les champs suivants :

- Username : Le nom d'utilisateur choisi par l'utilisateur.
- User : Un lien vers le modèle utilisateur par défaut de Django, facilitant l'accès aux fonctionnalités utilisateur intégrées telles que l'authentification et les permissions.

En utilisant ces modèles, l'application organise et gère efficacement les données relatives aux locations et aux utilisateurs, facilitant la récupération et la manipulation d'informations efficaces.