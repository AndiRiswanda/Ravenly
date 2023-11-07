from hero import Warrior, Assassin, Support

warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)
# sebelum
print("health (before)", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.get_health())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.get_health())
print("Support (speed) : ",support.get_speed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())




