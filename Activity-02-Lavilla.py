import random

print ("\nPokemon Calculator")
print ("\nA Lv. 90 Charizard (Fire/Flying, Sp. Atk: 205) attacks a Lv. 95")
print ("\nFeraligatr (Water, Sp. Def: 188) with Fire Blast, a Fire-type move ")
print ("\nwith a Power of 110 and gains a same-type attack bonus.. It hits ")
print ("\nthe target normally but deals a not very effective damage. The ")
print ("\nweather on the field is normal. Given the following conditions, ")
print ("\ndetermine how much damage Charizard’s attack will deal.")
print ("\nCharizard VS. Feraligatr")

Level = 90
SAtt = 205
SDef = 188
Power = 110
Targets = 1
Weather = 1
Badge = 1
critical = 1,2
crit = random.choice(critical)
rand = .85,1
rando = random.choice(rand)
Stab = 1
Type = 1

burned = [.5 , 1]
burn = random.choice(burned)
if burn == .5:
            print ("\n BURNEEEEEEEEEEED!!!")

Other = 1

Modifier = Targets * Weather * Badge * crit * rando * Stab * Type * burn * Other

Damage = ((((((2*Level)/5)+2)* Power * SAtt / SDef)/50)+2) * Modifier
print ("\nThe Damage of Charizard to Feligatr:  ", Damage , "\n\n\n\n")