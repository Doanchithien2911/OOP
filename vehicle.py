class Vehicle:
    def __init__(self,name,label):
        self._name=name
        self._label=label
        
    @property
    def name(self):
        return self._name
    
    @property
    def label(self):
        return self._label
    
class Specific(Vehicle):
    def __init__(self,name,label,capacity,price):
        super().__init__(name, label)
        self._capacity=capacity
        self._price=price
        
    @property
    def capacity(self):
        return self._capacity
    
    @property 
    def price(self):
        return self._price
n=int(input("nhap so luong : "))
listcar=[]
list_price=[]
for i in range(0,n):
    name=str(input("nhap ten xe thu {} ".format(i)))
    label=str(input("nhap hang xe thu {} ".format(i)))
    capacity=int(input("nhap so ghe cua xe thu {} ".format(i)))
    price=int(input("nhap gia tien cua xe thu {} ".format(i)))
    xe=Specific(name,label,capacity,price)
    listcar.append(xe)
    list_price.append(int(xe.price))
maxprice=max(list_price)
print("xe co gia cao nhat la {0} voi gia cao nhat la {1}".format(listcar[list_price.index(maxprice)].name,maxprice))    

    
    
    