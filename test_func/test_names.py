
from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Joseph", "Smith") == "Smith; Joseph"
    assert make_full_name("Joseph", "Smith-Junior") == "Smith-Junior; Joseph"
    assert make_full_name("Ágatha", "Alves-Reis") == "Alves-Reis; Ágatha"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Reis; Amon-Nobre") == "Reis"
    assert extract_family_name("Souza; Fernando-Silva") == "Souza"

def test_extract_given_name():
    assert extract_given_name("Reis; Amon") == "Amon"
    assert extract_given_name("Silva-Souza; Fernando") == "Fernando"
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
 