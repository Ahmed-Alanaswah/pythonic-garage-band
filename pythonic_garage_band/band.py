
class Band:
    instances=[]
    def __init__(self,name,members=[]) :
        self.name=name
        self.members=members
        Band.instances.append(self)
    
    def play_solos(self):
        solos = []
        for i in  self.members :
            solos.append(i.play_solo())

        return solos
       

    def __str__(self):
        pass
    def __repr__(self):
        pass
    
    @classmethod
    def to_list(cls):

        return cls.instances

class Musician(Band):
    def __init__(self,name) :
        super().__init__(name)
        
    def get_instrument(self):
        pass


    def play_solo(self):
        pass

    
class Guitarist(Musician):
     def __init__(self,name) :
         super().__init__(name)

     def __str__(self):

        return f"My name is {self.name} and I play guitar"
      
     def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

     def get_instrument(self):
        return "guitar"
     def play_solo(self):
        return "face melting guitar solo"
class Bassist(Musician):
    def __init__(self,name) :
         super().__init__(name)
    def __str__(self):

        return f"My name is {self.name} and I play bass"
      
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self,name) :
         super().__init__(name)
    def __str__(self):

        return f"My name is {self.name} and I play drums"
      
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash"

Joan = Guitarist("Joan Jett")
Meshell = Bassist("Meshell Ndegeocello")
Sheila = Drummer("Sheila E.")
nirvana=Band("Nirvana")
print(str(Joan))
print(repr(Joan))

print(str(Meshell))
print(repr(Meshell))

print(str(Sheila))
print(repr(Sheila))


