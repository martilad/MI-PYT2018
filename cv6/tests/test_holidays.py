
import pytest
import isholiday

@pytest.mark.parametrize('year', (2015, 2016, 2017, 2033, 2048))
def test_xmas(year):
    """Test whether there is Christmas"""
    holidays = isholiday.getholidays(year)
    assert (24, 12) in holidays