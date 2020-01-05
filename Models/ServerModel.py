import os


class Server:
    def __init__(self, device, size):
        self.size = float(size)
        self.memory = 0
        self.upload_time = self.size * 30
        self.directory = r'C:\Users\nasty\PycharmProjects\Bilbords\Server' + '\\' + device
        self.data = []
        try:
            os.mkdir(self.directory)
        except:
            pass
