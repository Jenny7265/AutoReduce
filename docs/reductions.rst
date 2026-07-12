.. currentmodule:: autoreduce

**********
Reductions
**********

AutoReduce implements reduction algorithms in `autoreduce.reductions`.

Time-Scale Separation
=====================

`reductions.timescale.Reduce` is the main reduction object for QSSA-style
time-scale separation workflows.

Conservation Laws
=================

Conservation-law reduction can be applied with
`reductions.conservation.solve_conservation_laws` or with
`reductions.timescale.Reduce.solve_conservation_laws`.

Projection Methods
==================

Projection-based DMD and DMDc wrappers are implemented in
`autoreduce.reductions.projection.dmd`. They require the `dmd` extra.

.. code-block:: bash

   pip install "autoreduce[dmd]"

Abundance-Based Methods
=======================

The `autoreduce.reductions.abundance` module marks the package location for
abundance-based reduction methods. The implementation currently raises
`NotImplementedError` until the algorithm is added.
