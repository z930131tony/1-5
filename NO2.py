class baggage:
    def __init__(self,ID,重量,出發機場,目的地機場,所屬旅客姓名):
        self._ID=ID
        self._重量=重量
        self._出發機場=出發機場
        self._目的地機場=目的地機場
        self._所屬旅客姓名=所屬旅客姓名

    
def main():
    行李1=baggage(1,7,"桃園機場","紐約機場","王大明")
    行李2=baggage(2,7,"台南機場","新加坡機場","劉小炫")
    行李3=baggage(3,7,"桃園機場","紐約機場","王小護")
    
#查詢行李
def getbaggage(self,ID):
    print("ID是:", self._ID)
    print("重量:", self._重量)
    print("出發機場:", self._出發機場)
    print("目的地機場:", self._目的地機場)
    print("姓名:", self._所屬旅客姓名)    
#修改資訊    

def getbaggage(self):
        print("ID是:", self._ID)
        print("重量:", self._重量)
        print("出發機場:", self._出發機場)
        print("目的地機場:", self._目的地機場)
        print("姓名:", self._所屬旅客姓名)

def modifybaggage(self,newID):
        
        self._ID = newID
def modifybaggage(self,new重量):
        
        self._重量 = new重量    
def modifybaggage(self,new出發機場):
        
        self._出發機場 = new出發機場     
def modifybaggage(self,new目的地機場):
        
        self._目的地機場 = new目的地機場   
def modifybaggage(self,new所屬旅客姓名):
        
        self._所屬旅客姓名 = new所屬旅客姓名        
        
        print("ID是:", self._newID)
        print("重量:", self._new重量)
        print("出發機場:", self._new出發機場)
        print("目的地機場:", self._new目的地機場)
        print("姓名:", self._new所屬旅客姓名)
        
        
                
        
        
class boardingpass:

    def __init__(self,姓名,登機證編號,登機時間,登機門編號,座位第n排,行李數量,行李ID):
        self._姓名=姓名
        self._登機證編號=登機證編號
        self._登機時間=登機時間
        self._登機門編號=登機門編號
        self._座位第n排=座位第n排
        self._行李數量=行李數量
        self._行李ID=行李ID
        