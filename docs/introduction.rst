Introduction
============

AutoReduce helps construct smaller dynamical models from larger symbolic
models. The central object is a nonlinear system written as

.. math::

   \dot{x} = f(x, \theta, u), \qquad y = h(x, \theta, u),

where ``x`` is the state vector, ``theta`` is the parameter vector, ``u`` is an
optional input, and ``y`` is the measured or designed output.

Why Reduce A Model?
-------------------

Detailed mechanistic models often contain states and parameters that are
necessary for construction but not necessary for the analysis question. A
reduced model can make simulation, parameter studies, controller design, and
scientific interpretation more tractable.

AutoReduce is intended for reductions where the resulting equations matter.
The reduced system is returned as symbolic dynamics, so users can inspect the
assumptions, simplify expressions, simulate the model, and compare it against
the original system.

Reduction Methods
-----------------

AutoReduce currently provides:

- Time-scale separation for quasi-steady-state approximation (QSSA).
- Conservation-law reduction for invariant total quantities.
- Local sensitivity analysis for ranking parameter effects.
- Projection-based DMD and DMDc interfaces through PyDMD.

Model Sources
-------------

Models can be constructed directly with SymPy expressions. AutoReduce also
provides compatibility modules for common scientific modeling workflows:

- SBML import and export through python-libsbml.
- BioCRNpyler integration through SBML files.
- python-control `NonlinearIOSystem` conversion through the ``control`` extra.
- PyDMD and DMDc workflows through the ``dmd`` extra.

When To Use AutoReduce
----------------------

Use AutoReduce when the model equations are part of the scientific result:
for example, when reducing biochemical reaction networks, comparing candidate
QSSA reductions, applying conservation laws before simulation, or connecting a
symbolic model to a data-driven projection method.
