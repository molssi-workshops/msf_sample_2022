
import pytest

import numpy as np

@pytest.fixture(scope="function")
def methane_molecule():
    symbols = np.array(["C", "H", "H", "H", "H"])
    coordinates = np.array(
        [[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]]
    )
    return symbols, coordinates