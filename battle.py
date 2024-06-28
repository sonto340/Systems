from char import stats
from enemies import current_enemy
#
#
#
hit_chance = 65

roll = (stats["acc"] - current_enemy["acc"])
if "hit_chance" < "roll":
    hit = False
elif "hit_chance" > "roll":
    hit = False
print(hit)
