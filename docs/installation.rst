Installation
============

Requirements
------------

AutoReduce requires Python 3.9 through 3.12 and the following dependencies:

* python-libsbml
* sympy
* scipy
* numpy<2

Optional dependencies (for visualization and advanced features):

* matplotlib
* seaborn
* biocrnpyler, for BioCRNpyler model construction workflows
* control, for python-control `NonlinearIOSystem` adapters
* pydmd, for DMD and DMDc projection workflows

Basic Installation
------------------

You can install AutoReduce using pip:

.. code-block:: bash

    pip install autoreduce

Or install from source:

.. code-block:: bash

    git clone https://github.com/ayush9pandey/AutoReduce.git
    cd AutoReduce
    pip install .

Development Installation
------------------------

For development, install the package in editable mode with the dependencies
needed for the task:

.. code-block:: bash

    git clone https://github.com/ayush9pandey/AutoReduce.git
    cd AutoReduce
    pip install -e ".[dev]"

Use the feature extras explicitly when working on optional integrations:

.. code-block:: bash

    pip install -e ".[bio]"
    pip install -e ".[control]"
    pip install -e ".[dmd]"

Verifying Installation
-----------------------

To verify your installation, you can run Python and import the package:

.. code-block:: python

    import autoreduce
    print(autoreduce.__version__)

If you don't see any errors, the installation was successful.

Troubleshooting
---------------

If you encounter any issues during installation:

1. Make sure you have Python 3.9 through 3.12 installed
2. Try creating a fresh virtual environment
3. Check that the extra for the feature you are using is installed
4. If using conda, you might need to install some packages through conda instead of pip

For more help, please open an issue on the `GitHub repository <https://github.com/ayush9pandey/AutoReduce/issues>`_.
