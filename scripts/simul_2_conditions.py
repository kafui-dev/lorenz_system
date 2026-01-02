from scripts import lorenz_solutions as ls

#------------------INITIALIZATION------------------
# parameters
params = {
    "sigma": 10,
    "b": 8/3,
    "r": 28,
    "N": 15000,
    "T": 60
}

# initial conditions
init1 = {
    "x0": 0,
    "y0": 1,
    "z0": 1.05
}
init2 = {
    "x0": 0,
    "y0": -1,
    "z0": 1.05
}

print(f"#------------------INITIALIZATION------------------\n"
      f"Parameters: {params}\n"
      f"Initial conditions 1: {init1}\n"
      f"Initial conditions 2: {init2}\n")

#------------------RESOLUTION------------------

X1 = ls.lorenz_system_with_euler(init1, params)
X2 = ls.lorenz_system_with_euler(init2, params)

#------------------PLOTTING------------------
ls.plot_solutions(X1[0], X1[1], X1[2], "simul_2_cond/simul2C-C1")
ls.plot_solutions(X2[0], X2[1], X2[2], "simul_2_cond/simul2C-C2")
print(f"#------------------RESOLUTION AND PLOTTING------------------\n"
      f"See solutions plot in plots/simul_2_cond\n")

#------------------ANALYSIS AND COMPARISON------------------
init3 = {
    "x0": 0,
    "y0": 1.001,
    "z0": 1.05
}
print(f"#------------------ANALYSIS AND COMPARISON------------------\n"
      f"Compaaring: Initial conditions 1: {init1}\n versus\n"
      f"Initial conditions 3: {init3}\n")

X3 = ls.lorenz_system_with_euler(init3, params)
ls.plot_comparison(X1[0], X3[0],
                   "x(t) for 1st initial conditions", "x(t) for 2nd initial conditions",
                   "simul_2_cond/x(t)_2_conditions")

print(f"See solutions plot in plots/simul_2_cond/x(t)_2_conditions.png\n")

