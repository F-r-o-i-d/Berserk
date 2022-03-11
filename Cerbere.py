
import logging
import socket
import parser
import ssl

logging = logging.Logger()
class SimpleServer:
    def __init__(self, target, port,verbose=False, ssl_https=False, ssl_cert="",ssl_key="") -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.address = (target, port)
        self.headers = []
        self.root = {}
        self.file = []
        self.ssl_https = ssl_https
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key
        self.verbose = verbose
    def __handler(self, socket):
        pass
    def AddHeaders(self, headers):
        self.headers.append(headers)
    def AddRoot(self, path, func):
        self.root[path] = func
    def __GeneratePayload(self, html_code, statue_code = "200 ok"):
        payload = "HTTP/1.0 "
        payload += statue_code
        payload += "\r\n"
        for x in self.headers:
            payload += x + "\r\n"
        payload += "\r\n"
        payload += html_code
        return payload.encode()
    def AutorizeFile(self, path):
        self.file.append(path)
    def run(self):
        """
        
        run server
        
        """
        if(self.ssl_https):
            self.sock = ssl.wrap_socket(self.sock, server_side=True, keyfile=self.ssl_key, certfile=self.ssl_cert)
        self.sock.bind(self.address)
        self.sock.listen(5)
        logging.info("server start")
        if(self.verbose):
            print(f"Running on {self.address}")
        while(1):
            sock, addr = self.sock.accept()

            req = sock.recv(1024)
            req = parser.request_parser(req)
            logging.info(f"request {addr} : {req[0]}")

            try:
                payload = self.__GeneratePayload(self.root[req[0]]((req[0],req[1])))
            except KeyError:
                try:
                    if(str(req[0])[1::] in self.file):
                        payload = self.__GeneratePayload(open(str(req[0])[1::],"r").read())
                    else:
                        payload = self.__GeneratePayload("404","404 Not Found")

                except Exception as e:
                    payload = self.__GeneratePayload("404","404 Not Found")
                    print(e)
            sock.sendall(payload)
            sock.close()
        logging.end()

