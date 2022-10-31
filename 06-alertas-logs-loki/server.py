# Python 3 server example
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time
import requests
import json
import datetime
import pytz
import random

def info():
	return 'INFO'

def warning():
	return 'WARNING'

def error():
	return 'ERROR'
    
logType = {
	200: info,
	201: warning,
	202: error
}

def pushToLoki(msg):
    host = 'ariel-pc'
    curr_datetime = datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg'))
    curr_datetime = curr_datetime.isoformat('T')

    code = random.randint(200, 202)
    userid = random.randint(1, 3)
    
    logTypeTxt = logType.get(code, error)()
    logToPush = '[{logTypeTxt}] code={code} userId={userId} log={msg}'.format(logTypeTxt=logTypeTxt,code=code,userId=userid,msg=msg)

    # push msg log into grafana-loki
    url = 'http://<IP_SERVER>:3100/api/prom/push'
    headers = {
        'Content-type': 'application/json'
    }
    payload = {
        'streams': [
            {
                'labels': '{source=\"PythonApp\",job=\"Cliente-01\", host=\"' + host + '\"}',
                'entries': [
                    {
                        'ts': curr_datetime,
                        'line': logToPush
                    }
                ]
            }
        ]
    }
    payload = json.dumps(payload)
    answer = requests.post(url, data=payload, headers=headers)
    print(answer)
    response = answer
    print(response)

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        query_string = parse_qs(urlparse(self.path).query)
        print("query_string " , query_string)
        try:        
            log = query_string["txt"][0]
            print("log= ", log)
            pushToLoki(log)
        except:
            pass
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")