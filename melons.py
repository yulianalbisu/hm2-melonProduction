import robots


class Melon(object):
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self): #def ___repr___(self)
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.melon_type)

# FIXME: Add Squash class definition here.

class Squash(Melon):
    
    def prep(self): #defining the special 'prep' procedure

        super().prep() #give a squash class(baby) a special 'prep' procedure, all the mom plus, prep added
        robots.painterbot.paint(self)


test_squash = Melon('Squash') #test squash is a made up variable to run my new class(nombre de uno de los de la lista)
test_squash.prep() #test.nueva orden() no olvides parentesis
other_test = Melon('Watermelon') #otro ejemplo, tiene otra variable nombre
other_test.prep()
