class Hero: 
    pass

hero_1 = Hero() 
hero_2 = Hero() 

hero_1.name = "Goku"
hero_2.name = "Naruto"

hero_1.power = 100
hero_2.power = 200


print(hero_1.name)
print(hero_1.power)  

print(hero_2.__dict__) 