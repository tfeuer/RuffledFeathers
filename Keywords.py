class Keywords:
    def __init__(filename):
        self.filename = filename
        self.array = []

        with open(self.filename) as f:
            for line in f:
                self.array.append(line)
