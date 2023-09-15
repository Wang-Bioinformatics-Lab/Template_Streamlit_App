## Wang Lab Streamlit Basic Template

This is a minimally viable template for Wang Lab

### Editing Template

1. Replace all references to template to your own name
1. Change the external port in docker-compose.yml and docker-compose-dev.yml
1. Make new repo
1. Bring up the server with ```make server-compose-interactive```
1. For Production, we don't open ports, everything goes through a reverse proxy, so you can use the following command ```make server-compose-production```

