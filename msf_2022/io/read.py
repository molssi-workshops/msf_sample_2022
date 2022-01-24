"""
Functions for reading molecular files
"""

import numpy as np

import matplotlib.pyplot as plt


def read_pdb(f_loc: str)->tuple[list[str], np.ndarray]:
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if "ATOM" in l[0:6] or "HETATM" in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)
    coords = np.array(c)
    return sym, coords

def read_xyz(file_location):
    #Open an xyz file and return symbols and coordinates
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype="unicode")
    symbols = xyz_file[:, 0]
    coords = xyz_file[:, 1:]
    coords = coords.astype(np.float)
    return symbols, coords