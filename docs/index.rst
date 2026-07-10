#######################################################
AutoReduce - Automated Dynamical Model Reduction Tools
#######################################################

AutoReduce is a Python package for automated reduction of symbolic
dynamical systems and SBML-derived models. It focuses on scientifically
explicit workflows for time-scale separation, conservation-law reduction,
local sensitivity analysis, and projection-based interfaces to established
reduction libraries.

.. rubric:: Features

- Symbolic model representation for nonlinear ODE systems.
- Numerical ODE and sensitivity solvers.
- Time-scale separation and conservation-law reduction routines.
- SBML import/export utilities through python-libsbml.
- Optional adapters for python-control `NonlinearIOSystem` models.
- Optional projection-based DMD and DMDc workflows through PyDMD.

.. rubric:: Links

- Source code: https://github.com/ayush9pandey/AutoReduce
- Documentation: https://autoreduce.readthedocs.io/
- Issue tracker: https://github.com/ayush9pandey/AutoReduce/issues

.. toctree::
   :caption: User Guide
   :maxdepth: 1
   :numbered: 2

   installation
   usage
   systems
   solvers
   reductions
   examples

.. toctree::
   :caption: Reference Manual
   :maxdepth: 1

   library
   develop
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
