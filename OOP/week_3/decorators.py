from abc import ABC , abstractmethod



class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()



class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        stats['Endurance'] += 7
        stats['Strength'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        stats['Perception'] -= 3
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        return stats

    def get_positive_effects(self):
        positiv = self.base.get_positive_effects()
        positiv.append('Berserk')
        return positiv



class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Endurance'] += 2
        stats['Strength'] += 2
        stats['Agility'] += 2
        stats['Luck'] += 2
        stats['Perception'] += 2
        stats['Charisma'] += 2
        stats['Intelligence'] += 2
        return stats

    def get_positive_effects(self):
        positiv = self.base.get_positive_effects()
        positiv.append('Blessing')
        return positiv



class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Endurance'] -= 4
        stats['Strength'] -= 4
        stats['Agility'] -= 4
        return stats

    def get_negative_effects(self):
        negativ = self.base.get_negative_effects()
        negativ.append('Weakness')
        return negativ


class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Endurance'] -= 2
        stats['Strength'] -= 2
        stats['Agility'] -= 2
        stats['Luck'] -= 2
        stats['Perception'] -= 2
        stats['Charisma'] -= 2
        stats['Intelligence'] -= 2
        return stats

    def get_negative_effects(self):
        negativ = self.base.get_negative_effects()
        negativ.append('Curse')
        return negativ



class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_negative_effects(self):
        negativ = self.base.get_negative_effects()
        negativ.append('EvilEye')
        return negativ




hero = Hero()
print(hero.get_stats())


brs1 = Berserk(hero)
print(brs1.get_stats())
print(brs1.get_positive_effects())

brs2 = Berserk(brs1)
print(brs2.get_stats())


brs3 = Berserk(brs2)
print(brs3.get_stats())

print(brs3.get_positive_effects())

cur1 = Curse(brs2)
print(cur1.get_stats())

print(cur1.get_positive_effects())

print(cur1.get_negative_effects())

cur1.base = brs1

print(cur1.get_positive_effects())