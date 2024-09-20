from names1 import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    
    assert make_full_name("Amon", "Reis") == "Reis; Amon"
    assert make_full_name("Mishael", "Hernandez-Garcia") == "Hernandez-Garcia; Mishael"
    assert make_full_name("Gabe", "Williams") == "Williams; Gabe"


def test_extract_family_name():

    assert extract_family_name("Reis; Amon") == "Reis"
    assert extract_family_name("Hernandez-Garcia; Mishael") == "Hernandez-Garcia"
    assert extract_family_name("Williams; Gabe") == "Williams"


def test_extract_given_name():

    assert extract_given_name("Reis; Amon") == "Amon"
    assert extract_given_name("Hernandez-Garcia; Mishael") == "Mishael"
    assert extract_given_name("Williams; Gabe") == "Gabe"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
