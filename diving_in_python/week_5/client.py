import socket
import time


class ClientError(Exception):
   pass


class Client:
    def __init__(self, ip, port, timeout = None):
        self.sock = socket.create_connection((ip, port), timeout)



    def read(self):
        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.sock.recv(1024)
            except socket.error as err:
                raise ClientError("error recv data", err)
        decoded_data = data.decode()

        status, payload = decoded_data.split("\n", 1)
        payload = payload.strip()

       
        if status == "error":
            raise ClientError(payload)

        return payload


    def get(self, metrika):
        try:
            self.sock.sendall(f"get {metrika}\n".encode())
        except:
            raise ClientError

        # print(status)
        answer = self.read()
        # print(answer)
        if answer == "":
            return {}
        d = dict()
        value = float()
        timestamp = int()
        for str in answer.split('\n'):
            print(str)
            try:
                key, value, timestamp = str.split(' ')
                timestamp = int(timestamp)
                value = float(value)
            except:
                raise ClientError
            if key not in d:
                d[key] = []
            d[key].append((int(timestamp), float(value)))
        dd = dict()
        val = list(())
        print(d)
        for key in d:
            mas = sorted(d[key])
            dd[key] = mas
        return dd



    def put(self, metrika, value, timestamp = None):
        timestamp = timestamp or int(time.time())
        try:
            self.sock.sendall(f"put {metrika} {value} {int(timestamp)}\n".encode())
        except:
            raise ClientError
        self.read()

        def close(self):
            try:
                self.sock.close()
            except socket.error as err:
                raise ClientError("error close connection", err)



def _main():
    client = Client("127.0.0.1", 8888, timeout=5)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
    d = client.get("*")


if __name__ == "__main__":
    _main()