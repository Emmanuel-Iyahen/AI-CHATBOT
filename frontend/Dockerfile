FROM nginx:alpine
COPY ./ /usr/share/nginx/html
# Copy your custom nginx.conf into the correct place
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
