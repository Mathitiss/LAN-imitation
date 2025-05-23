class Server:
    def __init__(self):
        self.data = []
        self.ip = id(self)

    def send_data(self, info):
        self.info = info

    def get_data(self):
        return self.data
        
    def get_ip(self):
        return self.ip

class Router:
    buffer = []

    @classmethod
    def link(cls, server):
        cls.buffer.append(server)

    @classmethod
    def unlink(cls, server):
        cls.buffer.remove(server)
    
    def send_data(cls):
        pass
        #cls.buffer[]

class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


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