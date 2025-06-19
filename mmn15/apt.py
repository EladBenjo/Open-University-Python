class Apt:
    """
    Represents an apartment with a floor number and area in square meters.
    """

    SQM_PRICE = 20000
    FLOOR_PRICE = 5000

    def __init__(self, floor, area):
        """
        Initialize an apartment.

        :param floor: The floor number of the apartment.
        :param area: The area of the apartment in square meters.
        """
        self._floor = floor
        self._area = area

    def get_floor(self):
        """
        Get the floor number of the apartment.

        :return: The floor number.
        """
        return self._floor

    def get_area(self):
        """
        Get the area of the apartment.

        :return: The area in square meters.
        """
        return self._area

    def __eq__(self, other):
        """
        Compare this apartment to another for equality.

        :param other: Another apartment instance.
        :return: True if both floor and area are equal, False otherwise.
                 Returns NotImplemented if types do not match.
        """
        if type(other) is not type(self):
            return NotImplemented
        return (self._floor, self._area) == (other.get_floor(), other.get_area())

    def __str__(self):
        """
        Return a string representation of the apartment.

        :return: String with floor and area details.
        """
        return f"floor: {self._floor}, area: {self._area}"

    def get_price(self):
        """
        Calculate the price of the apartment.

        :return: The total price, including floor surcharge if applicable.
        """
        floor_surcharge = self._floor * self.FLOOR_PRICE if self._floor > 1 else 0
        return self._area * self.SQM_PRICE + floor_surcharge
