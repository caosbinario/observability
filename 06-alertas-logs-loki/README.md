# Alertas logs con loki

Para ejecutar lo visto en el video deben hacer lo siguiente:

Levantamos grafana y loki:
```
docker-compose up -d
```
Por defecto, grafana va a levantarse en el puerto 3000 y genera el usuario y contraseña "admin" "admin"

Luego vamos al archivo [server.py](server.py) y editamos la linea 39 con la URL del servidor de Loki.
Y levantamos el servicio de python.
Recuerden instalar las dependencias, ahora no recuerdo cuales eran, pero les va a saltar que faltan las librerias y las instalan.
```
python server.py
```

Para tirar logs desde la app a loki, tienen que pegarle a la URL del servidor con el parametro "txt" y el valor del log.
Ejemplo:
http://localhost:8080?txt="app-log"

La aplicación es bastante básica, cuando le llega una petición genera un número random, del 1 al 3, y depende que número sea, escribe el log como INFO, WARNING o ERROR.
