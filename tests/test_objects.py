import numpy as np  # type: ignore

from autoreduce.solvers.ode import ODE
from autoreduce.solvers.ssm import SSM
from autoreduce.system.system import System
from autoreduce.utils.converters import load_ODE_model


def test_solver_objects_from_symbolic_model():
    """Build ODE and SSM solver objects from a symbolic system."""
    x, f, params = load_ODE_model(2, 2)
    f[0] = -(x[0] ** 2) + params[0] * x[1]
    f[1] = -params[1] * x[1]
    output_matrix = np.array([[0, 1]]).tolist()
    system = System(x, f, params=params, C=output_matrix)

    timepoints = np.linspace(0, 4, 3)
    params_values = [2, 4]
    x_init = [0, 10]

    ode_solver = ODE(
        system.x,
        system.f,
        params=system.params,
        params_values=params_values,
        C=system.C,
        x_init=x_init,
        timepoints=timepoints,
    )
    ssm_solver = SSM(
        system.x,
        system.f,
        params=system.params,
        params_values=params_values,
        C=system.C,
        x_init=x_init,
        timepoints=timepoints,
    )

    assert isinstance(ode_solver.solve_system(), np.ndarray)
    assert isinstance(ssm_solver.compute_J([2, 1]), np.ndarray)
    assert isinstance(ssm_solver.compute_Zj([2, 1], 1), np.ndarray)
