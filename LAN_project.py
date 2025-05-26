class Server:
    def __init__(self):
        self.buffer = []
        self.ip = id(self)
        self.router = None

    def send_data(self, info):
        if self.router:
            self.router.buffer.append(info)

    def get_data(self):
        d = self.buffer[:]
        self.buffer.clear
        return d
        
    def get_ip(self):
        return self.ip

class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        s = self.servers.pop(server.ip, False)
        if s:
            server.router = None
    
    def send_data(self):
        for i in self.buffer:
            if i.ip in self.servers:
                self.servers[i.ip].buffer.append(i)
        self.buffer.clear

class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

'''
TEST:

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
'''