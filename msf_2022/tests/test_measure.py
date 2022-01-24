"""
Tests for the measure module
"""

import numpy as np

import pytest

import msf_2022 as sp



def test_calculate_angle():
    """Test the calculate_angle function"""

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_value = 90

    calculated_value = sp.calculate_angle(r1, r2, r3, degrees=True)
    assert expected_value == calculated_value

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = sp.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(calculated_angle), F'{calculated_angle} {expected_angle}'