from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify if the make_full_name function works correctly.
    Parameters: None
    Return: Nothing
    """
    # Call the make_full_name function 3 times and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct each time.
    assert make_full_name("Amon Alves Dos", "Reis") == "Reis; Amon Alves Dos"
    assert make_full_name("Mishael Hernandez", "Garcia" ) == "Garcia; Mishael Hernandez"
    assert make_full_name("Gabe", "Williams") == "Williams; Gabe"


def test_extract_family_name():
    """Verify if the extract_family_name function works correctly.
    Parameters: None
    Return: Nothing
    """
    # Call the extract_family_name function 3 times and use an assert
    # statement to verify that the string returned by the
    # extract_family_name function is correct each time.
    assert extract_family_name("Reis; Amon Nobre") == "Reis"
    assert extract_family_name("Garcia; Mishael Hernandez") == "Garcia"
    assert extract_family_name("Williams; Gabe") == "Williams"


def test_extract_given_name():
    """Verify if the extract_given_name function works correctly.
    Parameters: None
    Return: Nothing
    """  
    # Call the extract_given_name function 3 times and use an assert
    # statment to verify that the string returned by the
    # extract_given_name function is correct each time.
    assert extract_given_name("Reis; Amon Alves Dos") == "Amon Alves Dos"
    assert extract_given_name("Garcia; Mishael Hernandez") == "Mishael Hernandez"
    assert extract_given_name("Williams; Gabe") == "Gabe"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
