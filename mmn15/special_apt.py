from apt import Apt


class SpecialApt(Apt):
    """
    Represents a special apartment with a view option, in addition to floor and area.
    """

    VIEW_PRICE = 600

    def __init__(self, floor, area, has_view):
        """
        Initialize a special apartment.

        :param floor: The floor number of the apartment.
        :param area: The area of the apartment in square meters.
        :param has_view: True if the apartment has a view, False otherwise.
        """
        super().__init__(floor, area)
        self._has_view = has_view

    def get_has_view(self):
        """
        Get whether the apartment has a view.

        :return: True if the apartment has a view, False otherwise.
        """
        return self._has_view

    def __eq__(self, other):
        """
        Compare this special apartment to another for equality.

        :param other: Another SpecialApt instance.
        :return: True if all attributes are equal, False otherwise.
                 Returns NotImplemented if types do not match.
        """
        if type(other) is not type(self):
            return NotImplemented
        same_apt = super().__eq__(other)
        return same_apt and self._has_view == other.get_has_view()

    def __str__(self):
        """
        Return a string representation of the special apartment.

        :return: String with all details, including view.
        """
        return f"{super().__str__()}, has_view: {self._has_view}"

    def get_price(self):
        """
        Calculate the price of the special apartment, including view surcharge.

        :return: The total price.
        """
        view_surcharge = self._floor * self.VIEW_PRICE if self._has_view else 0
        return super().get_price() + view_surcharge
