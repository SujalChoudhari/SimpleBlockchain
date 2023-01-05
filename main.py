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

    def __repr__(self):
        result = f" [{self.date}, {self.data}] "
        return result


class Blockchain:
    def __init__(self, date):
        self.head = Block(0, date, 'Head Block')
        self.chain = [self.head]

    def createBlock(self, id, date, data):
        block = Block(id, date, data, self.chain[-1].hash)
        self.chain.append(block)

    def __repr__(self):
        result = ""
        for block in self.chain:
            result += "->"
            result += block.__repr__()
        return result

test = Blockchain("8/7/2022")
test.createBlock(1,"8/7/22","Test")
test.createBlock(2,"8/7/22","Test2")
test.createBlock(3,"10/7/22","Test3")
test.createBlock(4,"11/7/22","Test4")
test.createBlock(5,"8/8/22","Test5")
test.createBlock(6,"8/9/22","Test6")

print(test)


