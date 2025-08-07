#!/bin/sh

# Generate the final servers.json from template using env vars
envsubst < /pgadmin4/servers.json.template > /pgadmin4/servers.json

# (Optional) Set proper permissions
chmod 600 /pgadmin4/servers.json
