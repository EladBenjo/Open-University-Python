from special_apt import SpecialApt


class GardenApt(SpecialApt):
    """
    Represents a garden apartment, which is a special apartment with a garden area.
    """

    def __init__(self, area, garden_area):
        """
        Initialize a garden apartment.

        :param area: The area of the apartment in square meters.
        :param garden_area: The area of the garden in square meters.
        """
        # Garden apartments are always on floor 0 and do not have a view.
        super().__init__(0, area, False)
        self._garden_area = garden_area

    def get_garden_area(self):
        """
        Get the area of the garden.

        :return: The garden area in square meters.
        """
        return self._garden_area

    def __eq__(self, other):
        """
        Compare this garden apartment to another for equality.

        :param other: Another GardenApt instance.
        :return: True if all attributes are equal, False otherwise.
                 Returns NotImplemented if types do not match.
        """
        if type(other) is not type(self):
            return NotImplemented
        same_special = super().__eq__(other)
        return same_special and self._garden_area == other.get_garden_area()

    def __str__(self):
        """
        Return a string representation of the garden apartment.

        :return: String with all details, including garden area.
        """
        return f"{super().__str__()}, garden_area: {self._garden_area}"
    