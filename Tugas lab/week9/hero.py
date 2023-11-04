class human:
    def __init__(self,nama,pos_x = 0):
        self.name = nama
        self.__position = pos_x = 0
    #positioning
    def getPosition(self):
        return self.__position
    def changePosition(self,value):
        self.__position = value

    #Tactics
    def attack(self, target):
        target._health -= self._power    
    def movement(self,vertex):
        if vertex.upper() == "L":
            self.__position -= self._speed
        elif vertex.upper() == "R":
            self.__position += self._speed

    #Getter
    def get_power(self):
        return self._power
    def get_health(self):
        return self._health
    def get_armor(self):
        return self._armor
    def get_speed(self):
        return self._speed

    #setter
    def set_power(self,value):
        self._power = value
    def set_health(self,value):
        self._health = value
    def set_armor(self,value):
        self._armor = value
    def set_speed(self,value):
        self._speed = value
               
class Hero(human):
    def __init__ (self,nama,pos_x = 0):
        super().__init__(nama,pos_x = 0)
        self._power = 15
        self._health = 100
        self._armor = 5
        self._speed = 3

class Warrior(human):
    def __init__ (self,nama,pos_x = 0):
        super().__init__(nama,pos_x = 0)
        self._power = 20
        self._health = 150
        self._armor = 10
        self._speed = 4

    def special (self,target):
        self._armor += 35
        self._power += 12
        target.power -= self._power

class Assassin(human):
    def __init__ (self,nama,pos_x = 0):
        super().__init__(nama,pos_x = 0)
        self._power = 20
        self._health = 100
        self._armor = 5
        self._speed = 5

    def special (self,target):
        self._speed += 2
        self._power += 22
        target._health -= self._power

class Support(human):
    def __init__ (self,nama,pos_x = 0):
        super().__init__(nama,pos_x = 0)
        self._power = 10
        self._health = 500
        self._armor = 30
        self._speed = 2

    def special (self,target):
        self._speed += 2
        target._health -= self._power
        






