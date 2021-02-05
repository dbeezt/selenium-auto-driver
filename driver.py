import platform
import webbrowser

class Driver():
    example_browsers = ['firefox', 'chromium', 'chrome']

    def __init__(self, browsers = example_browsers):
        self.os = self.which_os()
        self.browser = self.detect_browser(browsers = browsers)

    def which_os(self):
        os = platform.system()
        def map_os(os):
            return {
                'Windows': 'windows',
                'Linux': 'linux',
                'Darwin': 'mac'
            }.get(os, None)
        return map_os(os)

    def detect_browser(self, browsers):
        for browser in browsers:
            try:
                webbrowser.get(using = browser)
            except Exception as e:
                print(f"Webbrowser Error: {e}")
            else:
                return browser
        
        return None
        

class Gecko(Driver):
    def __init__(self, **args):
        super().__init__()
        print(self.browser)


class Chromium(Driver):
    def __init__(self, **args):
        super().__init__()
        print(self.os)


Gecko()