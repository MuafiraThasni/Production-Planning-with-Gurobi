# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:55:59 2021

@author: muafi
"""
import pyomo.environ as pyo
import numpy as ny
from pyomo.opt import SolverFactory
from pyomo.environ import *

model = pyo.ConcreteModel(name = 'Cell_and_Desk_Production')
model.desk = pyo.Var(bounds=(100,ny.inf))
model.cell = pyo.Var(bounds=(100,ny.inf))
model.overtime = pyo.Var(bounds = (0,40))
d = model.desk
c = model.cell
overtime = model.overtime

model.c1 = pyo.Constraint(expr = 0.2*d + 0.4*c <= 400+overtime)
model.c2 = pyo.Constraint(expr = 0.5*d + 0.4*c <= 490)
#model.c3 = pyo.Constraint(expr = overtime <= 40)

model.obj = pyo.Objective(expr = 12*d + 20*c-2*overtime, sense=maximize)

opt=SolverFactory('gurobi')
opt.solve(model)

model.pprint

desk_production = pyo.value(d)
cell_production = pyo.value(c)

print('desk production = ', desk_production)
print('cell production = ', cell_production)

