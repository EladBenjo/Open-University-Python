from special_apt import SpecialApt


class RoofApt(SpecialApt):
    """
    Represents a rooftop apartment, which is a special apartment with an optional pool.
    """

    ROOF_PRICE = 40000
    POOL_PRICE = 30000

    def __init__(self, floor, area, has_pool):
        """
        Initialize a rooftop apartment.

        :param floor: The floor number of the apartment.
        :param area: The area of the apartment in square meters.
        :param has_pool: True if the apartment has a pool, False otherwise.
        """
        # Rooftop apartments always have a view (True passed to SpecialApt)
        super().__init__(floor, area, True)
        self._has_pool = has_pool

    def get_has_pool(self):
        """
        Get whether the rooftop apartment has a pool.

        :return: True if the apartment has a pool, False otherwise.
        """
        return self._has_pool

    def __eq__(self, other):
        """
        Compare this rooftop apartment to another for equality.

        :param other: Another RoofApt instance.
        :return: True if all attributes are equal, False otherwise.
                 Returns NotImplemented if types do not match.
        """
        if type(other) is not type(self):
            return NotImplemented
        same_special = super().__eq__(other)
        return same_special and self._has_pool == other.get_has_pool()

    def __str__(self):
        """
        Return a string representation of the rooftop apartment.

        :return: String with all details, including pool status.
        """
        return f"{super().__str__()}, has_pool: {self._has_pool}"

    def get_price(self):
        """
        Calculate the price of the rooftop apartment, including roof and pool surcharges.

        :return: The total price.
        """
        pool_surcharge = self.POOL_PRICE if self._has_pool else 0
        return super().get_price() + self.ROOF_PRICE + pool_surcharge
