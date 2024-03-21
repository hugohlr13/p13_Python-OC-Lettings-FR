.. _installation:

Installation & Prérequis
========================

- Compte GitHub avec accès en lecture à ce dépôt
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande ``python`` de votre shell OS exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

macOS / Linux
-------------

**Cloner le dépôt**

.. code-block:: bash

   cd /path/to/put/project/in
   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

**Créer l'environnement virtuel**

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   python -m venv venv
   apt-get install python3-venv  # Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu

**Activer l'environnement**

.. code-block:: bash

   source venv/bin/activate

**Vérifier l'environnement**

.. code-block:: bash

   # Confirmer que la commande 'python' exécute l'interpréteur Python dans l'environnement virtuel
   which python

   # Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure
   python --version

   # Confirmer que la commande 'pip' exécute l'exécutable pip dans l'environnement virtuel
   which pip

**Pour désactiver l'environnement**

.. code-block:: bash

   deactivate

**Exécuter le site**

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pip install --requirement requirements.txt
   python manage.py runserver

**Tester le site**

Ouvrez http://localhost:8000 dans un navigateur. Confirmez que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
