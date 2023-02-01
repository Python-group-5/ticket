class Railway:
    def __init__(self,tno,pname,price,jfto,cate):
        self.tic_no=int(tno)
        self.pass_name=pname
        self.journey_to=jfto
        self.tic_price=float(price)
        self.cat=cate

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)
    
