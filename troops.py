
# Help: ID, Name, Alias, TribeID, Speed, Attack, Defi, Defc, Carry

troops = [[0, "Phalanx", ["Phalanx", "phalanx", "Phal", "phal", "Phals", "phals"], 0, 7, 15, 40, 50, 35],
          [1, "Swordsman", ["Swordsman", "swordsman", "Sword", "sword", "Swords", "sword"], 0, 6, 65, 35, 20, 45],
          [2, "Pathfinder", ["Pathfinder", "pathfinder", "Spy", "spy"], 0, 17, 0, 20, 10, 0],
          [3, "Theutates Thunder", ["Theutates Thunder", "Thunder", "thunder", "tt", "TT"], 0, 19, 90, 25, 40, 75],
          [4, "Druidrider", ["Druidrider", "druidrider", "druid", "Druid"], 0, 16, 45, 115, 55, 35],
          [5, "Haeduan", ["Haeduan", "haeduan"], 0, 13, 140, 60, 165, 65],
          [6, "Ram", ["Ram", "ram"], 0, 4, 50, 30, 105, 0],
          [7, "Trebuchet", ["Trebuchet", "trebuchet", "Catapult", "catapult", "Cata", "cata", "Cat", "cat"], 0, 3, 70, 45, 10, 0],
          [8, "Chieftain", ["Chieftain", "chieftain", "Chief", "chief"], 0, 5, 40, 50, 50, 0],
          [9, "Settler", ["Settler", "settler"], 0, 5, 0, 80, 80, 3000],
          [10, "Legionnaire", ["Legionnaire", "legionnaire", "Leg", "leg", "Legs", "legs"], 1, 6, 40, 35, 50, 50],
          [11, "Praetorian", ["Praetorian", "praetorian", "Praet", "praet"], 1, 5, 30, 65, 35, 20],
          [12, "Imperian", ["Imperian", "imperian", "Imp", "imp"], 1, 7, 70, 40, 25, 50],
          [13, "Equites Legati", ["Equites Legati", "EL", "el", "Legati", "legati", "Spy", "spy"], 1, 16, 0, 20, 10, 0],
          [14, "Equites Imperatoris", ["Equites Imperatoris", "EI", "Imp", "imp"], 1, 14, 120, 65, 50, 100],
          [15, "Equites Caesaris", ["Equites Caesaris", "EC", "Caesaris", "caesaris"], 1, 10, 180, 80, 105, 70],
          [16, "Battering Ram", ["Battering Ram", "Ram", "ram"], 1, 4, 60, 30, 75, 0],
          [17, "Fire Catapult", ["Fire Catapult", "Catapult", "catapult", "Cata", "cata", "Cat", "cat"], 1, 3, 75, 60, 10, 0],
          [18, "Senator", ["Senator", "senator", "Chief", "chief"], 1, 4, 50, 40, 30, 0],
          [19, "Settler", ["Settler", "settler"], 1, 5, 0, 80, 80, 3000],
          [20, "Clubswinger", ["Clubswinger", "clubswinger ", "Club", "club", "Clubs", "clubs"], 2, 7, 40, 20, 5, 60],
          [21, "Spearman", ["Spearman", "spearman", "Spear", "spear", "Spears", "spears"], 2, 7, 10, 35, 60, 40],
          [22, "Axeman", ["Axeman", "axeman", "Axe", "axe"], 2, 6, 60, 30, 30, 50],
          [23, "Scout", ["Scout", "scout", "Spy", "spy"], 2, 9, 0, 10, 5, 0],
          [24, "Paladin", ["Paladin", "paladin"], 2, 10, 55, 100, 40, 110],
          [25, "Teutonic Knight", ["Teutonic Knight", "TK", "Teutonic", "teutonic"], 2, 9, 150, 50, 75, 80],
          [26, "Ram", ["Ram", "ram"], 2, 4, 65, 30, 80, 0],
          [27, "Catapult", ["Catapult", "catapult", "Cata", "cata", "Cat", "cat"], 2, 3, 50, 60, 10, 0],
          [28, "Chief", ["Chief", "chief"], 2, 4, 40, 60, 40, 0],
          [29, "Settler", ["Settler", "settler"], 2, 5, 10, 80, 80, 3000]]

# Help: ID, Name, Alias

tribes = [[0, "Gaul", ["Gaul", "G", "g", "gaul"]],
          [1, "Roman", ["Roman", "R", "r", "roman"]],
          [2, "Teuton", ["Teuton", "T", "t", "teuton"]]]


def name(id):
    if (len(troops) > id) and (id >= 0):
        return troops[id][1]


def alias(id):
    if (len(troops) > id) and (id >= 0):
        return troops[id][2]


def tribe(id):
    if (len(troops) > id) and (id >= 0):
        return tribes[troops[id][3]][1]


def idbycall(call):
    answer = []
    for troop in troops:
        if call in troop[2]:
            answer.append(troop[0])
    return answer


def idbycalltribefilter(call):
    answer = []
    for i in range(0, len(tribes)):
        answer.append([i])
    for troop in troops:
        if call in troop[2]:
            answer[troop[3]].append(troop[0])
    return answer


def speed(id):
    if (len(troops) > id) and (id >= 0):
        return troops[id][4]


def tribename(id):
    if (len(tribes) > id) and (id >= 0):
        return tribes[id][1]


def tribeidbycall(call):
    answer = []
    for tribe in tribes:
        if call in tribe[2]:
            answer.append(tribe[0])
    return answer
