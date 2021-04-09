L=[1,2,4,7,8,9]

def vider(stock):
    if stock==[]:
        return "erreur"
    else:
        while len(stock)>0:
            print(stock[0])
            stock=stock[1:]
    
        

vider(L)
