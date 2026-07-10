"""Conservation-law reduction entry points."""

from autoreduce.reductions.timescale import Reduce


def solve_conservation_laws(reducible_system: Reduce, **kwargs) -> Reduce:
    """Apply conservation laws to a `Reduce` system.

    Parameters
    ----------
    reducible_system
        Reducible AutoReduce system.
    kwargs
        Arguments forwarded to `Reduce.solve_conservation_laws`.

    Returns
    -------
    Reduce
        The same system with conservation laws applied.
    """
    if not isinstance(reducible_system, Reduce):
        raise TypeError("reducible_system must be an autoreduce Reduce object.")
    return reducible_system.solve_conservation_laws(**kwargs)
