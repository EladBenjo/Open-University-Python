from apt import Apt
from special_apt import SpecialApt
from garden_apt import GardenApt
from roof_apt import RoofApt

TRESHOLD_PRICE = 1000000


def average_price(apts):
    """
    Calculate the average price of a list of apartments.

    :param apts: List of apartment objects (must implement get_price()).
    :return: Average price as float, or 0 if the list is empty.
    """
    total = 0
    count = 0
    for apt in apts:
        total += apt.get_price()
        count += 1
    if count == 0:
        return 0
    average = total / count
    return average


def how_many_rooftop(apts):
    """
    Count the number of rooftop apartments that has pool in a list of apartments

    :param apts: List of apartment objects
    :return: Number of rooftop apartments with pool
    """
    count = 0
    for apt in apts:
        if isinstance(apt, RoofApt):
            if apt.get_has_pool():
                count += 1
    return count


def how_many_apt_type(apts):
    """
    Count the number of apartments of each type in the list.

    :param apts: List of apartment objects.
    :return: Dictionary with keys 'Apt', 'SpecialApt', 'GardenApt', 'RoofApt' and their counts as values.
    """
    counts = {
        'Apt': 0,
        'SpecialApt': 0,
        'GardenApt': 0,
        'RoofApt': 0
    }
    for apt in apts:
        # Important: Start with the most specific types first,
        # because isinstance(roof_apt, SpecialApt) and isinstance(roof_apt, Apt) are also True.
        if isinstance(apt, GardenApt):
            counts['GardenApt'] += 1
        elif isinstance(apt, RoofApt):
            counts['RoofApt'] += 1
        elif isinstance(apt, SpecialApt):
            counts['SpecialApt'] += 1
        elif isinstance(apt, Apt):
            counts['Apt'] += 1
    return counts


def top_price(apts):
    """
    Find and return the first instance of apartment with the highest price in a list of apartments

    :param apts: List of apartment objects
    :return: 'None' if the list is empty else 'apt' object with the higest price
    """
    top = 0
    res = None
    for apt in apts:
        price = apt.get_price()
        if price > top:  # use '>' to return the first highest price apartment
            top = price
            res = apt
    return res


def only_valid_apts(apts):
    """
    Iterating through list of apartments and returning a list with qualifying apartments
    Qualifications: Apartment has view or pool, and it's priced over one million shekels
    :param apts:
    :return:
    """
    res = []
    for apt in apts:
        # since any apartment that has pool, already has view, check if SpecialApt, and check if it has view.
        if isinstance(apt, SpecialApt):
            if apt.get_has_view() and apt.get_price() > TRESHOLD_PRICE:
                res.append(apt)
    return res if res else None
