import platform


class  Driver():
    def __init__(self, **args):
        self.os = self.which_os()

    def which_os(self):
        os = platform.system()
        def map_os(os):
            return {
                'Windows': 'windows',
                'Linux': 'linux',
                'Darwin': 'mac'
            }.get(os, None)
        return map_os(os)
        

class Gecko(Driver):
    def __init__(self, **args):
        super().__init__()
        print(self.os)


class Chromium(Driver):
    def __init__(self, **args):
        super().__init__()
        print(self.os)