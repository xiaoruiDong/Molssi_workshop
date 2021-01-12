"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np

@pytest.fixture(scope="module")
def methane():
    symbols  = np.array(['C', 'H', 'H', 'H', 'H',])
    coords = np.array([
   	 [0, 0, 0,],
   	 [1, 0, 0,],
   	 [-1, 0, 0,],
   	 [1, 0, 1],
	 [0, -1, 0],])

@pytest.mark.skip
def test_build_bond(methane):
    symbols, coords = methane
    with pytest.raises(RuntimeError):
    	bonds = molecool.build_bond_list(coords, min_bond=-1)

def test_build_bond_failure():
    coords = np.array([
   	 [0, 0, 0,],
   	 [1, 0, 0,],
   	 [-1, 0, 0,],
   	 [1, 0, 1],])

    with pytest.raises(RuntimeError):
    	
    	bonds = molecool.build_bond_list(coords, min_bond=-1)

def test_build_bond_list():

    coords = np.array([
    	[0, 0, 0,],
	[1, 0, 0,],
	[-1, 0, 0,],
	[1, 0, 1],])
    bonds = molecool.build_bond_list(coords, max_bond=1.4)
    
    assert len(bonds) == 3
    for bond_length in bonds.values():
    	assert bond_length == 1.0

def test_calculate_distance():
    """Test that the calculate distance function."""
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 0, 1])

    expected_distance = 1
    observed_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == observed_distance


def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules
