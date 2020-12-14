import json


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
        self._houseing = None
        self._amenities = None
        self._power = None
        self._appeal = None
        self._bonus = None
        self._strategic = None
        self._luxury = None
        self._trader = None

    # erah
    @property
    def erah(self):
        if self._erah == None:
            return None
        return self._erah

    @erah.setter
    def erah(self, value):
        self._erah = value

    # govener        
    @property
    def govener(self):
        if self._govener == None:
            return None
        return self._govener

    @govener.setter
    def govener(self, value):
        self._govener = value

    # food        
    @property
    def food(self):
        if self._food == None:
            return None
        return self._food

    @food.setter
    def food(self, value):
        self._food = value

    # production        
    @property
    def production(self):
        if self._production == None:
            return None
        return self._production

    @production.setter
    def production(self, value):
        self._production = value

    # gold        
    @property
    def gold(self):
        if self._gold == None:
            return None
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

    # science        
    @property
    def science(self):
        if self._science == None:
            return None
        return self._science

    @science.setter
    def science(self, value):
        self._science = value

    # culture        
    @property
    def culture(self):
        if self._culture == None:
            return None
        return self._culture

    @culture.setter
    def culture(self, value):
        self._culture = value

    # faith        
    @property
    def faith(self):
        if self._faith == None:
            return None
        return self._faith

    @faith.setter
    def faith(self, value):
        self._faith = value

    # tourism        
    @property
    def tourism(self):
        if self._tourism == None:
            return None
        return self._tourism

    @tourism.setter
    def tourism(self, value):
        self._tourism = value

    # population        
    @property
    def population(self):
        if self._population == None:
            return None
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    # houseing        
    @property
    def houseing(self):
        if self._houseing == None:
            return None
        return self._houseing

    @houseing.setter
    def houseing(self, value):
        self._houseing = value

    # amenities        
    @property
    def amenities(self):
        if self._amenities == None:
            return None
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        self._amenities = value

    # power        
    @property
    def power(self):
        if self._power == None:
            return None
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    # appeal
    @property
    def appeal(self):
        if self._appeal == None:
            return None
        return self._appeal

    @appeal.setter
    def appeal(self, value):
        self._appeal = value

    # bonus        
    @property
    def bonus(self):
        if self._bonus == None:
            return None
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        self._bonus = value

    # strategic        
    @property
    def strategic(self):
        if self._strategic == None:
            return None
        return self._strategic

    @strategic.setter
    def strategic(self, value):
        self._strategic = value

    # luxury        
    @property
    def luxury(self):
        if self._luxury == None:
            return None
        return self._luxury

    @luxury.setter
    def luxury(self, value):
        self._luxury = value

    # trader        
    @property
    def trader(self):
        if self._trader == None:
            return None
        return self._trader

    @trader.setter
    def trader(self, value):
        self._trader = value
        
