class Character:
    """ A representation of a user's progression through levels. Each member
    will have a character object attached to it. """

    titles = ['Crook', 'Soldier', 'Capo', 'Underboss', 'Mafia Boss',
              'Head Mafia Boss']

    def __init__(self, name, lvl):
        # python interprets level as a string, so I'm typecasting for now
        self.level = int(lvl)
        self.meta_level = self.titles[0]
        self.tag = "Lvl " + str(self.level) + " "
        self.nick = name
        self.tag_nick = self.tag + self.nick

    def update_tag_nick(self):
        self.tag_nick = self.tag + self.nick

    def update_level(self, delta):
        self.level = min(100, max(1, self.level + delta))
        self.meta_level = self.titles[int(self.level / 20)]
        self.tag = "Lvl " + str(self.level) + " "
        self.update_tag_nick()

    def update_nick(self, nickname):
        self.nick = nickname
        self.update_tag_nick()
