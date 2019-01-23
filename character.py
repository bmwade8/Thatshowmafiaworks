class Character:
    """ A representation of a user's progression through levels. Each member
    will have a character object attached to it. """

    titles = ['Crook', 'Soldiers', 'Capo', 'Underboss', 'Mafia Boss',
              'Head Mafia Boss']

    def __init__(self, name):
        self.level = 1
        self.meta_level = self.titles[0]
        self.nick = "Lvl 1 " + name

    def update_level(self, delta):
        if (self.level + delta) < 1:
            self.level = 1
        else:
            self.level += delta
        self.meta_level = self.titles[int(self.level / 20)]
        self.update_nick(self.nick[6:])

    def update_nick(self, nickname):
        self.nick = "Lvl " + str(self.level) + " " + nickname
