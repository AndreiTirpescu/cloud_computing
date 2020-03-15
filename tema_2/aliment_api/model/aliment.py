class Aliment:
    def __init__(self, id, name, price, code):
        self.id             = id
        self.name           = name
        self.price          = price
        self.code           = code

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
    
    def getCode(self):
        return self.code

    def get_dict(self):
        return {
            "name"  : self.name,
            "price" : self.price,
            "code"  : self.code
        }