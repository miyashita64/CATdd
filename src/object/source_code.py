class SourceCode:
    def __init__(self, path, code):
        self.path = path
        self.code = code
        self.lines = code.split("\n")