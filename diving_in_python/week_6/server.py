import asyncio
from collections import defaultdict
from copy import deepcopy

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()



class ClientServerProtocol(asyncio.Protocol):
    data = defaultdict(dict)
    def __init__(self):
        super().__init__()
        self._buffer = ''

    def connection_made(self, transport):
        self.transport = transport

    def get_parser(self, text):
        if text == '*':
            return deepcopy(self.data)
        if text in self.data:
            return {text: deepcopy(self.data.get(text))}
        return {}


    def put_parser(self, params):
        print(params)
        key, value, timestamp = params
        try:
            value, timestamp = float(value), int(timestamp)
            self.data[key][timestamp] = value
            print(self.data[key][timestamp])
        except:
            raise ValueError

    def process(self, method, params):
        if method == "put":
            print("количество: " + str(len(params)))
            self.put_parser(params)
            return {}
        elif method == "get":
            key = params.pop()
            if params:
                raise ValueError
            return self.get_parser(key)
        else:
            raise ValueError



    def data_received(self, data):
        self._buffer = data
        message = ''
        try:
            text = self._buffer.decode('utf-8')

            if not text.endswith('\n'):
                return
            text3 = text.rstrip('\n')
            method, *params = text3.split()
            data_ = self.process(method, params)
            message = ''
            if method == 'get':
                for key, values in data_.items():
                    message += '\n'.join(f'{key} {value} {timestamp}' \
                                             for timestamp, value in sorted(values.items()))
                    message += '\n'
                    print(message)

            code = 'ok'
        except (ValueError, UnicodeDecodeError, IndexError) as er:
            print(er)
            message = 'wrong command\n'
            code = 'error'

        response = f'{code}\n{message}\n'
        print('respone: ' + response)
        # отправляем ответ
        try:
            self.transport.write(response.encode('utf-8'))
        except:
            return('oplaaaa')

if __name__ == "__main__":
    run_server('127.0.0.1', 8888)