class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate

    def sleep(h):
        if h==7:
            return("Happy")
        elif h>7:
            return("Lazy")
        else:
            return("Tired")
    
    def eat(m):
        if m>=3:
            return "100%hth"
        elif m==2:
            return "75%hth"
        elif m==1:
            return "50%hth"
        else:
            return "0%hth"
    
    def buy(self,i):
       self.money -=10*i
       return self.money
    
class Employee(Person):
    def __init__(self,id,car,salary,dtw,name, money, mood, healthRate):
        super().__init__(name, money, mood, healthRate)
        self.id=id
        self.car=car
        self.salary=salary
        self.dtw=dtw


    @property
    def email(self):
        return '{}@email.com'.format(self.name)


    def work(h):
        if h==8:
            return("Happy")
        elif h>8:
            return("Lazy")
        else:
            return("Tired")   

    def send_email(fro,t,sub,msg,recv_name):
        f=open('{}.txt'.format(sub), 'w')
        return f.write( "To: "+t+"\nFrom: "+fro+"\n\nHi,"+recv_name+"\n"+msg+"\nThanks.")
