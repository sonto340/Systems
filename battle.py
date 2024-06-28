from char import stats
from enemies import current_enemy
#
#
#
hit_chance = 65

roll = (stats["acc"] - current_enemy["acc"])
while "hit_chance" < "roll":
    hit = True
else:
    hit = False
print(hit)
