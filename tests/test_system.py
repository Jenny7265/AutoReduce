# Copyright (c) 2020, Ayush Pandey. All rights reserved.
# See LICENSE file in the project root directory for details.

import importlib

import numpy as np
import pytest

import autoreduce
from autoreduce.system.system import System


def test_system_equality(system_1):
    """Check that equivalent `System` objects compare equal."""
    system_copy = System(
        system_1.x,
        system_1.f,
        params=system_1.params,
        x_init=system_1.x_init,
        params_values=system_1.params_values,
        C=system_1.C,
        g=system_1.g,
        h=system_1.h,
        u=system_1.u,
        input_values=system_1.input_values,
    )
    assert system_1 == system_copy


def test_system_attributes(system_1):
    """Check that core symbolic system attributes are stored intact."""
    assert len(system_1.x) == 4
    assert len(system_1.f) == 4
    assert len(system_1.params) == 3
    assert system_1.params_values == [2, 4, 6]
    assert np.array_equal(system_1.x_init, np.ones(4))
    assert system_1.C is None
    assert system_1.g is None
    assert system_1.h is None
    assert system_1.u is None


def test_old_import_paths_are_not_exported():
    """Confirm the refactor does not preserve removed convenience imports."""
    assert not hasattr(autoreduce, "System")
    assert not hasattr(autoreduce, "load_ODE_model")
    assert not hasattr(importlib.import_module("autoreduce.system"), "System")
    assert not hasattr(importlib.import_module("autoreduce.utils"), "get_ODE")

    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("autoreduce.ode")

    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("autoreduce.model_reduction")
