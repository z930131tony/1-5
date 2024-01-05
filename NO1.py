class computer:
    #電腦類別的建構子
    #說明:用來建立該指定類別型態的函式，將相同類別的東西放入Class，可以去掉每次都要重新設定的麻煩性，後續如果需要修改也能一次改完
    def __init__(self,name,m,c) :
        #name=名稱, m=價格, c=數量
            self._name=name
            self._m=m
            self._c=c
    def count(self):
         #計算總價的函式
        return self._m*self._c
            
def main(): 
    computer1=computer("ROG",20000,2)      
    computer2=computer("Razer",30000,4)    
    computer3=computer("MSI",10000,1)    
    print(computer1._name)
    print("總價:",computer1.count())
    print(computer2._name)
    print("總價:",computer2.count())
    print(computer3._name)
    print("總價:",computer3.count())