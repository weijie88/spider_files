class Stock():
    def __init__(self,code,name,price):
        self.code = code
        self.name = name
        self.price = price
    def __str__(self):
        return 'code{},name{},price{}'.format(self.code,self.name,self.price)