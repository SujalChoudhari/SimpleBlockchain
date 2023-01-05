import hashlib


class Block:
    def __init__(self, id, date, data, previousHash=""):
        self.id = id
        self.date = date
        self.data = data
        self.previousHash = previousHash
        self.hash = self.newHash()

    def newHash(self):
        return hashlib.sha256((str(self.id) + self.date + self.data +
                               self.previousHash).encode("utf-8")).hexdigest()

        


class Blockchain:
    def __init__(self, date):
        self.head = Block(0, date, 'Head Block')
        self.chain = [self.head]

    def createBlock(self, id, date, data):
        block = Block(id, date, data, self.chain[-1].hash)
        self.chain.append(block)


test = Blockchain("8/7/2022")
test.createBlock(1,"8/7/22","Test")




