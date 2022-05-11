import sqlite3

boglanish = sqlite3.connect('mydatabase.db')
int = input("Malumotni kiriting: ")
name = boglanish.cursor()
# BIRINCHISI
name.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT
)            
                
                
""")

name.execute("""
INSERT INTO shopping VALUES   
('Azamjon', 'Ziyobiddinov'),            
('Azamjon', 'Ziyobiddinov'), 
('Azamjon', 'Ziyobiddinov') 
                
""")

name.execute("SELECT * FROM shopping")
# IKKINCHISI
meva = boglanish.cursor()
meva.execute("""
CREATE TABLE IF NOT EXISTS meva(
    name TEXT,
    last_name TEXT
)            
                
                
""")

meva.execute("""
INSERT INTO meva VALUES   
('NOK', '12000'),            
('OLMA', '10000'), 
('SHAFTOLI', '35000') 
                
""")

meva.execute("SELECT * FROM meva")
# Uchunchisi
car = boglanish.cursor()
car.execute("""
CREATE TABLE IF NOT EXISTS car(
    name TEXT,
    last_name TEXT
)            
                
                
""")

car.execute("""
INSERT INTO car VALUES   
('Malibu', 'M 700 XA'),            
('Spark', 'A 555 KA'), 
('Nexia', 'M 800 LA') 
                
""")

car.execute("SELECT * FROM car")

if int == 'car':
    print(car.fetchall())
    
elif int == 'name':
    print(name.fetchall())
    
elif int == 'meva':    
    print(meva.fetchall())
    
else:
    print("Bu malumot mavjut emas! ")  
    
    
    
    
    
    
    import threading as thr
import time

event = thr.Event() 

def list():
    time.sleep(1)
    event.wait()
    print("Siz dasturchi bo'lish uchun shularni o'raganishingiz kerak CSS JAVA HTML PHYTON BOTSTRAP... ")
    time.sleep(1)
    
javob = input("Dasturchi bo'lishni istaysizmi ")

t1 = thr.Thread(target=list)
t1.start() 

if javob == 'ha':
    event.set() 
else:
    print("Sizga omad tilymiz") 


def link():
    print("Qizil chiroq")
    time.sleep(1)
    print("3 soniya kuting")
    time.sleep(3)
    print("Sariq chiroq")
    print("2 soniya kuting")
    time.sleep(2)
    print("Yashil chiroq yondi")
    time.sleep(1)
    print("Yurishingiz mumkun: ")
    time.sleep(1)
    
link()   



class link:
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self , list):
        return link(self.x + list.x, self.y + list.y)
    
    def __repr__(self):
        return f"X ning qiymati {self.x} va Y ning qiymati {self.y}:" 
           
           
li1 = link(20, 30)
li2 = link(40, 20)           
li3 = link(10, 10) 
li4 = link(40, 20)
li5 = link(70, 60) 

print(li1 + li2 + li3 + li4 + li5) 

def decorative_function(func):
    def ichki(text):
        return [func(value[0], value[1],) for value in text] 
    return ichki

@decorative_function 
def number(a, b):
    print(a + b)  

print(number([(10, 20), (40, 50), (25, 55)]))




import threading


def link():
    for x in range(5):
        print("hello")
        
def link2():
    for x in range(5):        
        print("salom")

t1 = threading.Thread(target=link)
t2 = threading.Thread(target=link2)

t1.start()
t2.start()