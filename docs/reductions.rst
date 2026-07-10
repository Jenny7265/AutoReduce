.. currentmodule:: autoreduce

**********
Reductions
**********

Reduction algorithms live under `autoreduce.reductions`.

Time-Scale Separation
=====================

`reductions.timescale.Reduce` is the main reduction object for QSSA-style
time-scale separation workflows.

Conservation Laws
=================

Conservation-law routines are exposed through
`reductions.conservation.solve_conservation_laws` and the corresponding
methods on `reductions.timescale.Reduce`.

Projection Methods
==================

Projection-based DMD and DMDc wrappers live in
`autoreduce.reductions.projection.dmd` and require the `dmd` extra.

.. code-block:: bash

   pip install "autoreduce[dmd]"

Abundance-Based Methods
=======================

The `autoreduce.reductions.abundance` module marks the package location for
abundance-based reduction methods. The implementation currently raises
`NotImplementedError` until the algorithm is added.
