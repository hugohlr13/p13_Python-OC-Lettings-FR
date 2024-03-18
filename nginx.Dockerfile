# Utilisez l'image officielle nginx
FROM nginx:alpine

# Supprimez la configuration nginx par défaut
RUN rm /etc/nginx/conf.d/default.conf

# Copiez la configuration nginx personnalisée dans le conteneur
COPY nginx.conf /etc/nginx/conf.d

# Exposez le port 80 pour que votre application puisse être accessible
EXPOSE 80
