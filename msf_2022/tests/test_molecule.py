"""
Tests for the molecule module
"""

import numpy as np

import pytest

import msf_2022 as sp


def test_move_methane(methane_molecule):
    symbols, coordinates = methane_molecule

    coordinates[0] += 5

def test_build_bond_list(methane_molecule):

    _, coordinates = methane_molecule

    bonds = sp.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4


def test_build_bond_list_error():

    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )

    with pytest.raises(ValueError):
        bonds = sp.build_bond_list(coordinates, min_bond=-1)


def test_center_of_mass(methane_molecule):

    symbols, coordinates = methane_molecule

    center_of_mass = sp.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1, 1, 1])

    assert np.array_equal(center_of_mass, expected_center)


def test_molecular_mass(methane_molecule):

    symbols, _ = methane_molecule

    calculated_mass = sp.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass