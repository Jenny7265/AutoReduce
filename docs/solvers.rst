.. currentmodule:: autoreduce

*******
Solvers
*******

AutoReduce provides numerical solvers in `autoreduce.solvers`.

ODE Solver
==========

`solvers.ode.ODE` evaluates a symbolic `System` and solves the resulting ODE
with SciPy.

Sensitivity Solver
==================

`solvers.ssm.SSM` computes local sensitivity coefficients and Jacobian
approximations for symbolic systems.
