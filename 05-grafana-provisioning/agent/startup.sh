# comandos en tiempo real
echo '' >> ~/.bashrc
echo '#guardar los comandos en tiempo real' >> ~/.bashrc
echo 'shopt -s histappend' >> ~/.bashrc
echo 'PROMPT_COMMAND="history -a;$PROMPT_COMMAND"' >> ~/.bashrc

# descargar plugin
docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

