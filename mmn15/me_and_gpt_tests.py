from apt import Apt
from special_apt import SpecialApt
from garden_apt import GardenApt
from roof_apt import RoofApt


def test_eq_apt():
    a1 = Apt(2, 50)
    a2 = Apt(2, 50)
    a3 = Apt(3, 50)
    a4 = Apt(2, 60)
    assert a1 == a2, "Same floor/area should be equal"
    assert not (a1 == a3), "Different floor should not be equal"
    assert not (a1 == a4), "Different area should not be equal"
    assert not (a1 == "not an apt"), "Different type should be NotImplemented"


def test_eq_special_apt():
    s1 = SpecialApt(2, 100, True)
    s2 = SpecialApt(2, 100, True)
    s3 = SpecialApt(2, 100, False)
    s4 = SpecialApt(3, 100, True)
    a1 = Apt(2, 100)
    assert s1 == s2, "Same params, should be equal"
    assert not (s1 == s3), "Different has_view should not be equal"
    assert not (s1 == s4), "Different floor should not be equal"
    assert not (s1 == a1), "Different class (Apt) should be NotImplemented"


def test_eq_garden_apt():
    g1 = GardenApt(80, 25)
    g2 = GardenApt(80, 25)
    g3 = GardenApt(80, 30)
    s1 = SpecialApt(0, 80, False)
    assert g1 == g2, "Same area/garden should be equal"
    assert not (g1 == g3), "Different garden_area should not be equal"
    assert not (g1 == s1), "Different class should be NotImplemented"


def test_eq_roof_apt():
    r1 = RoofApt(10, 90, True)
    r2 = RoofApt(10, 90, True)
    r3 = RoofApt(10, 90, False)
    r4 = RoofApt(7, 90, True)
    s1 = SpecialApt(10, 90, True)
    assert r1 == r2, "Same params should be equal"
    assert not (r1 == r3), "Different has_pool should not be equal"
    assert not (r1 == r4), "Different floor should not be equal"
    assert not (r1 == s1), "Different class (SpecialApt) should be NotImplemented"


def test_eq_inheritance():
    r = RoofApt(5, 80, False)
    g = GardenApt(80, 30)
    s = SpecialApt(5, 80, True)
    assert not (r == s), "RoofApt and SpecialApt with same base fields should not be equal"
    assert not (g == s), "GardenApt and SpecialApt should not be equal"


def test_eq_random_type():
    a = Apt(1, 50)
    assert (a == 7) is False, "Comparison with int should be False/NotImplemented"
    assert (a == None) is False, "Comparison with None should be False/NotImplemented"


def test_eq_reflexive():
    a = Apt(4, 60)
    assert a == a, "Object should always equal itself"


if __name__ == "__main__":
    test_eq_apt()
    test_eq_special_apt()
    test_eq_garden_apt()
    test_eq_roof_apt()
    test_eq_inheritance()
    test_eq_random_type()
    test_eq_reflexive()
    print("All eq tests passed!")