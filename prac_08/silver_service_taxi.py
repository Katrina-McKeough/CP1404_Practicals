from prac_08.taxi import Taxi
from random import uniform


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but including flagfall."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                                                      self.current_fare_distance,
                                                                                      self.price_per_km, self.flagfall)

    def get_fare(self):
        """Return the price for the SilverServiceTaxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
