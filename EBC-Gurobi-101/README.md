# Table of Contents

1. [Introduction](#introduction)
1. [Modeling with gurobipy](#modeling-with-gurobipy)
    1. [Structure of models](#structure-of-models)
    1. [Adding variables](#adding-variables)
    1. [Objective functions](#objective-functions)
    1. [Adding constraints](#adding-constraints)
    1. [Setting parameters](#setting-parameters)
    1. [Solving a model](#solving-a-model)
    1. [Retrieving the solution](#retrieving-the-solution)
    1. [Debugging](#debugging)

﻿﻿**This is currently under construction**

# Introduction

This is a short tutorial on how to use Gurobi at our institute. 
We hereby aim at providing you the basics to formulate and understand models written with Gurobi's Python interface gurobipy.
An introduction to other modeling environments used at the EBC (pyomo, GAMS, and ortools) might follow later.
This is **not** a tutorial to teach you the basics of optimization or advanced modeling techniques for formulating optimization problems. 

We therefore assume that you have Gurobi and gurobipy installed on your computer.
We also assume that you are familiar with Python and therefore understand how to create functions, pass variables, handle lists, dictionaries, arrays, etc.
Furthermore, this tutorial shall introduce you to the basic concepts of gurobipy; thus, we do not dig into the advanced modeling improvements introduced in Gurobi 7.0. A section on this topic might however follow in the next versions of this  tutorial.

In this tutorial, we will cover the following aspects:

* general structure of models
* how to add variables
* how to specify an objective function
* how to add constraints to your model
* how to set solver parameters
* how to solve a model
* how to retrieve an optimal solution
* how to debug a model

[Go back :arrow_up:](#table-of-contents)

# Modeling with gurobipy

Gurobipy is a Python interface for the Gurobi optimizer.
With this framework, you can easily set up optimization problems in an easy-to-read manner.
Please note that the model you set up in Python is transferred automatically to the Gurobi optimizer that is coded in C/C++.
So, debugging is not as straightforward as with regular Python tools, since you cannot look into every line of code.
But, we will explain at the end of this tutorial, how to deal with model errors and how to debug your code.

[Go back :arrow_up:](#table-of-contents)

## Structure of models

Every gurobipy model is/should be written in a separate model file that is structured in the following way:

**First**, you start by importing gurobipy.
Some authors prefer to set a namespace, e.g. `gp`

``` python
import gurobipy as gp
```

**Next**, you define a function that receives preprocessed inputs:

``` python
def optimize(input_1, input_2, input_3):
   """ 
   This is my optimization model that is also commented in an exemplary manner.

   Parameter
   ---------
   input_1 ....
   """
```

The **third** part of your gurobipy is the creation of a new model.
Models are created with the `Model` function:

``` python
my_model = gp.Model("My model's name")
```

**Afterwards**, variables are created.

These variables have to be added to the model.
This is done by calling the `update` function at the end of this block:

``` python
my_model.update()
```

The **fifth** step is the definition of an objective function.
For instance, we can try to minimize a previously added variable, which we called `var`

``` python
my_model.setObjective(var, gp.GRB.MINIMIZE)
```

If we try to maximize an expression, we can either minimize it's negative value or use `gp.GRB.MAXIMIZE`.

The **sixth** step adds constraints to our model.

In a **seventh* step, we can optionally specify certain solver parameters.

**Next**, we solve our model and hope to receive an optimal solution.

If we succeed and our model is feasible and bounded, we can then retrieve our optimal solution in a **ninth** step.

If we fail, we have to conduct a debugging process in a **tenth** step and solve again.

The next chapters explain the most important steps in more detail.

[Go back :arrow_up:](#table-of-contents)

## Adding variables

After creating a new model, which we will call throughout the rest of this tutorial `model`, we add variables to this model.

We can either add variables that are not grouped within sets (e.g. `emissions`) or we can add variables with a logical relationship that can be addressed through sets (e.g. time-depending `temperatures`).

We **can add one continous variable** without grouping sets by writing the following line
``` python
emissions = model.addVar(vtype="C", lb=0, ub=1000, name="emi")
```

Hereby, a new variable, which we will refer to in the rest of this tutorial as `emissions` is created.
This variable is a continuous variable, which implies that it can take any value between a given lower bound (lb) and an upper bound (ub).
Furthermore, we assign an internal name *emi* to our variable.

Not every parameter is necessary in this line, however, some are very useful and should also be specified (!), whereas some are redundant or optional.

In this line, *vtype* sets the type of variable.
Next to `C` (which implies a continuous variable), we can also assign `B` for binary variables.
Note that there exist many more types of variables, but since this is a basic tutorial, we stick to these two types, since they are by far the most important types of variables.

A lower and an upper bound are specified.
Here, a lower bound of 0 is set.
This is not necessary, since 0 is the standard lower bound for all variables.
Please keep this in mind, especially, if your model contains variables that can become negative!!!
Additionally, an upper bound of 1000 is set.
This parameter (like the lower bound) is optional.
However, in contrast to the lower bound, this upper bound provides new information, since the standard value is 10^100 (which is stored in the variable gp.GRB.INFINITY).

Setting a name is also optional.
We strongly encourage you to do so, because it tremendously simplifies the debugging process.
The standard naming is a simple enumeration of all variables.
If you did not specify a unique name here, you might end up searching variable c10000 in a model with more than 10001 variables, which is hardly possible.
Therefore, please always set a **unique and unambiguous name** for your variables.

**Adding multiple variables** that are grouped with a set is straightforward.
For doing so, we first create an empty dictionary and add variables as entries of this dictionary:
``` python
temperatures = {}
for time in range(100):
    temperatures[time] = model.addVar(vtype="C", lb=-20, ub=100, name="temp_"+str(time))
```

This code snippet creates 100 variables called *temperature[0], temperature[1], ... temperature [99]*.
All of these variables have a lower bound of -20 and an upper bound of 100.
If you have specific bounds for each temperature, you can provide them by using a second list that holds these values.
The internal names of these temperatures are unique and unambiguous.
They are temp_0, temp_1, ... temp_99.

[Go back :arrow_up:](#table-of-contents)


[Go back :arrow_up:](#table-of-contents)
[Go back :arrow_up:](#table-of-contents)
[Go back :arrow_up:](#table-of-contents)
[Go back :arrow_up:](#table-of-contents)
[Go back :arrow_up:](#table-of-contents)
[Go back :arrow_up:](#table-of-contents)
[Go back :arrow_up:](#table-of-contents)