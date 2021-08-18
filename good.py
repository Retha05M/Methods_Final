class GoodBye:
    def __init__(self, name):
        self.name = name

    def goodbye_to(self):
        goodbye_msg = 'GoodBye ' + self.name
        return goodbye_msg
