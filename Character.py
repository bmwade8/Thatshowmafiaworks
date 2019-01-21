class Character:
    """ A representation of a user's progression through levels. Each member
    will have a character object attached to it. """

    titles = ['Crook', 'Soldiers', 'Capo', 'Underboss', 'Mafia Boss',
              'Head Mafia Boss']

    def __init__(self):
        self.level = 1
        self.meta_level = self.titles[0]

    def update_level(self, delta):
        self.level += delta
        self.meta_level = self.titles[int(self.level / 20)]
