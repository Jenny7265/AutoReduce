########################################################
AutoReduce: An Automated Model Reduction Toolbox
########################################################

AutoReduce is a Python package for constructing reduced-order models of
nonlinear dynamical systems. It is designed for scientific workflows where
the reduced model should remain interpretable: users provide symbolic system
equations, select states or constraints that define the reduction problem,
and obtain reduced dynamics that can be inspected, simulated, and exported.

The package supports model reduction by time-scale separation, conservation
laws, abundance assumptions, local sensitivity analysis, and projection-based
interfaces to established model-reduction libraries. AutoReduce is not tied to
one model source: models can be written directly as SymPy expressions or
imported through supported compatibility layers.

.. rubric:: Core capabilities

- Symbolic representation of nonlinear ordinary differential equation models.
- Numerical simulation of full and reduced systems.
- Quasi-steady-state approximation (QSSA) through time-scale separation.
- Conservation-law reduction for systems with invariant total quantities.
- Local sensitivity analysis for parameter-dependent systems.
- Projection-based DMD and DMDc workflows through PyDMD.

.. rubric:: Background

AutoReduce was introduced for automated construction of phenomenological
models from more detailed biological circuit descriptions. The original
workflow combines time-scale separation, conservation laws, and species
abundance assumptions to produce smaller models that retain the input-output
relationships needed for design analysis [PandeyMurray2020]_.

The robustness tools in AutoReduce are connected to structured model
reduction guarantees for dynamical systems, with biomolecular examples
developed in [PandeyMurray2023]_. Projection-based workflows use PyDMD
[Demo2018]_, and the python-control adapter supports interoperability with
the python-control systems library [Fuller2021]_.

Compatibility notes:

- SymPy is used for symbolic ODE definitions.
- SciPy is used for numerical ODE simulation.
- python-libsbml supports SBML import and export.
- BioCRNpyler models can be used through SBML-based workflows.
- python-control `NonlinearIOSystem` models are supported by the
  ``control`` extra.
- PyDMD-based DMD and DMDc reductions are supported by the ``dmd`` extra.

.. rubric:: Related research

.. [PandeyMurray2020] Ayush Pandey and Richard M. Murray. "Model Reduction
   Tools For Phenomenological Modeling of Input-Controlled Biological
   Circuits." bioRxiv, 2020. https://doi.org/10.1101/2020.02.15.950840

.. [PandeyMurray2023] Ayush Pandey and Richard M. Murray. "Robustness
   guarantees for structured model reduction of dynamical systems with
   applications to biomolecular models." *International Journal of Robust and
   Nonlinear Control*, 33(9):5058-5086, 2023.
   https://doi.org/10.1002/rnc.6013

.. [Demo2018] Nicola Demo, Marco Tezzele, and Gianluigi Rozza. "PyDMD:
   Python Dynamic Mode Decomposition." *Journal of Open Source Software*,
   3(22):530, 2018. https://doi.org/10.21105/joss.00530

.. [Fuller2021] Sawyer Fuller, Ben Greiner, Jason Moore, Richard Murray,
   Rene van Paassen, and Rory Yorke. "The Python Control Systems Library
   (python-control)." In *2021 60th IEEE Conference on Decision and Control
   (CDC)*, 4875-4881, 2021. https://doi.org/10.1109/CDC45484.2021.9683368

.. toctree::
   :caption: User Guide
   :maxdepth: 1
   :numbered: 2

   introduction
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
