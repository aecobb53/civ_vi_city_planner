

class CommonTile:

    def __init__(self):

        self._erah = None
        self._govener = None
        self._food = None
        self._production = None
        self._gold = None
        self._science = None
        self._culture = None
        self._faith = None
        self._tourism = None
        self._population = None
        self._housing = None
        self._citizen_slot = None
        self._amenities = None
        self._power = None
        self._powered = None
        self._appeal = None
        self._maintenance = None
        self._bonus = None
        self._strategic = None
        self._luxury = None
        self._trader = None

    # era
    @property
    def erah(self):
        if self._erah is None:
            return None
        return self._erah

    @erah.setter
    def erah(self, value):
        self._erah = value

    # govener
    @property
    def govener(self):
        if self._govener is None:
            return None
        return self._govener

    @govener.setter
    def govener(self, value):
        self._govener = value

    # food
    @property
    def food(self):
        if self._food is None:
            return 0
        return self._food

    @food.setter
    def food(self, value):
        self._food = value

    # production
    @property
    def production(self):
        if self._production is None:
            return 0
        return self._production

    @production.setter
    def production(self, value):
        self._production = value

    # gold
    @property
    def gold(self):
        if self._gold is None:
            return 0
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

    # science
    @property
    def science(self):
        if self._science is None:
            return 0
        return self._science

    @science.setter
    def science(self, value):
        self._science = value

    # culture
    @property
    def culture(self):
        if self._culture is None:
            return 0
        return self._culture

    @culture.setter
    def culture(self, value):
        self._culture = value

    # faith
    @property
    def faith(self):
        if self._faith is None:
            return 0
        return self._faith

    @faith.setter
    def faith(self, value):
        self._faith = value

    # tourism
    @property
    def tourism(self):
        if self._tourism is None:
            return 0
        return self._tourism

    @tourism.setter
    def tourism(self, value):
        self._tourism = value

    # population
    @property
    def population(self):
        if self._population is None:
            return 0
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    # housing
    @property
    def housing(self):
        if self._housing is None:
            return 0
        return self._housing

    @housing.setter
    def housing(self, value):
        self._housing = value

    # citizen_slot
    @property
    def citizen_slot(self):
        if self._citizen_slot is None:
            return 0
        return self._citizen_slot

    @citizen_slot.setter
    def citizen_slot(self, value):
        self._citizen_slot = value

    # amenities
    @property
    def amenities(self):
        if self._amenities is None:
            return 0
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        self._amenities = value

    # power
    @property
    def power(self):
        if self._power is None:
            return 0
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    # powered
    @property
    def powered(self):
        if self._powered is None:
            return False
        return self._powered

    @powered.setter
    def powered(self, value):
        self._powered = value

    # appea
    @property
    def appeal(self):
        if self._appeal is None:
            return 0
        return self._appeal

    @appeal.setter
    def appeal(self, value):
        self._appeal = value

    # maintenanc
    @property
    def maintenance(self):
        if self._maintenance is None:
            return 0
        return self._maintenance

    @maintenance.setter
    def maintenance(self, value):
        self._maintenance = value

    # bonus
    @property
    def bonus(self):
        if self._bonus is None:
            return None
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        self._bonus = value

    # strategic
    @property
    def strategic(self):
        if self._strategic is None:
            return None
        return self._strategic

    @strategic.setter
    def strategic(self, value):
        self._strategic = value

    # luxury
    @property
    def luxury(self):
        if self._luxury is None:
            return None
        return self._luxury

    @luxury.setter
    def luxury(self, value):
        self._luxury = value

    # trader
    @property
    def trader(self):
        if self._trader is None:
            return None
        return self._trader

    @trader.setter
    def trader(self, value):
        self._trader = value
