# AutoReduce: An automated model reduction tool

Python toolbox to obtain reduced model expressions using time-scale
separation, conservation laws, sensitivity analysis, and projection-based
interfaces to established reduction libraries.

[![Build](https://github.com/ayush9pandey/autoreduce/actions/workflows/build.yml/badge.svg)](https://github.com/ayush9pandey/autoreduce/actions/workflows/build.yml)
[![Lint](https://github.com/ayush9pandey/autoreduce/actions/workflows/lint.yml/badge.svg)](https://github.com/ayush9pandey/autoreduce/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/ayush9pandey/AutoReduce/graph/badge.svg?token=h9diSMrJbj)](https://codecov.io/gh/ayush9pandey/AutoReduce)
[![PyPI version](https://badge.fury.io/py/autoreduce.svg)](https://badge.fury.io/py/autoreduce)
[![Documentation Status](https://readthedocs.org/projects/autoreduce/badge/?version=latest)](https://autoreduce.readthedocs.io/en/latest/?badge=latest)

## Overview

AutoReduce is a Python package for automated model reduction of symbolic and
SBML-derived dynamical systems. It provides tools for:
- Automated model reduction using QSSA (Quasi-Steady State Approximation)
- Conservation-law based reductions
- Local sensitivity analysis
- Integration with [BioCRNPyler](https://biocrnpyler.readthedocs.io/) for synthetic biology models
- Optional python-control and PyDMD interfaces

Refer to the [bioRxiv paper](https://www.biorxiv.org/content/10.1101/2020.02.15.950840v2.full.pdf) and [Journal of Robust and Nonlinear Control paper](https://onlinelibrary.wiley.com/doi/full/10.1002/rnc.6013) for more details.

## Quick Start

```python
from autoreduce.utils.converters import load_sbml

# Load your SBML model
sys = load_sbml('your_sbml_file.xml', outputs=['your_output'])

# Solve conservation laws
conservation_laws = sys.solve_conservation_laws(
    conserved_sets=[
        ['species1', 'species2', 'species3'],  # First conserved set
        ['species4', 'species5']               # Second conserved set
    ],
    states_to_eliminate=['species_to_eliminate1', 'species_to_eliminate2']
)

# Solve timescale separation using QSSA
reduced_qssa_model = sys.solve_timescale_separation(
    ['fast_species1', 'fast_species2']
    )
```

For more examples, check out the [documentation](https://autoreduce.readthedocs.io/en/latest/examples.html).

## Installation

AutoReduce currently supports Python 3.9 through 3.12 with NumPy < 2, which
keeps it compatible with BioCRNpyler.

Install the latest version of AutoReduce:

```bash
pip install autoreduce
```

Install with all optional dependencies:

```bash
pip install autoreduce[all]
```

Install optional integrations explicitly:

```bash
pip install "autoreduce[bio]"
pip install "autoreduce[control]"
pip install "autoreduce[dmd]"
```

For development installation:

```bash
git clone https://github.com/ayush9pandey/autoreduce.git
cd autoreduce
pip install -e ".[dev]"
```

## Documentation

Full documentation is available at [autoreduce.readthedocs.io](https://autoreduce.readthedocs.io/).

## Contributing

We welcome contributions. Developer notes and release instructions are in the
[documentation](https://autoreduce.readthedocs.io/en/latest/develop.html).

## Contact

For questions, feedback, or suggestions, please contact:
- Ayush Pandey (ayushpandey at ucmerced dot edu)
- [GitHub Issues](https://github.com/ayush9pandey/autoreduce/issues)

## License

Released under the BSD 3-Clause License (see `LICENSE`)

Copyright (c) 2025, Ayush Pandey. All rights reserved.
