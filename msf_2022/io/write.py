"""
Functions for writing molecular files.
"""

def write_xyz(file_location, symbols, coordinates):

    # Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)

    if num_atoms != len(coordinates):
        raise ValueError(
            f"write_xyz : the number of symbols ({num_atoms}) and number of coordinates ({len(coordinates)}) must be the same to write xyz file!"
        )

    with open(file_location, "w+") as f:
        f.write("{}\n".format(num_atoms))
        f.write("XYZ file\n")

        for i in range(num_atoms):
            f.write("{}\t{}\t{}\t{}\n".format(symbols[i], coordinates[i, 0], coordinates[i, 1], coordinates[i, 2]))