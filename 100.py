class Car(object):
    def __init__ (self,model,color,company,speedlimit):
        self.color = color
        self.model = model
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
       print("started")     
    def stop(self):
       print("stopped")
    def accelerate(self):
       print("accelerating")   
    def gear(self,gear):
       print("gear changed")     

audi = Car("A3","red","audi","100")
print(audi.color)

audi.gear(3)