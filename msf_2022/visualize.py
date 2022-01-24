"""
Visualization functions
"""


import matplotlib.pyplot as plt  # type: ignore
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # type: ignore # noqa: F401
from typing import Optional

from msf_2022.atom_data import atom_colors

__all__ = ["draw_molecule", "bond_histogram"]


def draw_molecule(
    coordinates: np.ndarray,
    symbols: list[str],
    draw_bonds: Optional[dict] = None,
    save_location: Optional[str] = None,
    dpi: Optional[float] = 300,
) -> plt.Axes:
    """
    Draw molecule coordinates using matplotlib.

    Parameters
    ----------
    coordinates: np.ndarray
        The coordinates of the atoms
    symbols: list
        A list representing the elements of the molecule.
    draw_bonds: dict
        A dictionary containing bond information for the molecule.
    save_location: str, optional
        The location to save the graph.
    dpi: float, optional
        The resolution of the saved image.

    Returns
    -------
    plt.ax
        A matplotlib axis with the specified molecule drawn.
    """

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])

    size = np.array(plt.rcParams["lines.markersize"] ** 2) * 200 / (len(coordinates))

    ax.scatter(
        coordinates[:, 0],
        coordinates[:, 1],
        coordinates[:, 2],
        marker="o",
        edgecolors="k",
        facecolors=colors,
        alpha=1,
        s=size,
    )

    # Draw bonds
    if draw_bonds:
        for atoms in draw_bonds.keys():
            atom1 = atoms[0]
            atom2 = atoms[1]

            ax.plot(
                coordinates[[atom1, atom2], 0],
                coordinates[[atom1, atom2], 1],
                coordinates[[atom1, atom2], 2],
                color="k",
            )

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)

    return ax


def bond_histogram(
    bond_list: dict,
    save_location: Optional[str] = None,
    dpi: float = 300,
    graph_min: float = 0,
    graph_max: float = 2,
) -> plt.Axes:
    """
    Create a histogram showing the distribution of bond lengths for a molecule.

    Parameters
    ----------
    bond_list : dict
        A dictionary containing bond information.
    save_location: str, optional
        The file location to save the graph image.
    dpi: float, optional
        The resolution of the saved image.
    graph_min: float, optional
        The minimum y value of the graph.
    graph_max: float, optional
        The maximum y value of the graph.

    Returns
    -------
    plt.ax
        A matplotlib axis.
    """

    lengths = []
    for bond_length in bond_list.values():
        lengths.append(bond_length)

    bins = np.linspace(graph_min, graph_max)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.xlabel("Bond Length (angstrom)")
    plt.ylabel("Number of Bonds")

    ax.hist(lengths, bins=bins)

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)

    return ax
