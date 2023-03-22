class store:
    def __init__(self,id,price,stock):
        self.id=id
        self.price=price
        self.stock=stock

idf=[101,102,103,108]
prf=[42,50,500,40]
stf=[10,20,15,16]
lif=[]
for i in range(len(idf)):
    id=idf[i]
    price=prf[i]
    stock=stf[i]
    lif.append(store(id,price,stock))
protoser=int(input())
quan=int(input())
present=True
for products in lif:
    if products.id==protoser:
        present=False
        if products.stock-quan<0:
            print("No stock left")
        else:
            tot=float(products.price*quan)
            products.stock-=quan
            print(tot)

if present:
    print("Invalid input")   

