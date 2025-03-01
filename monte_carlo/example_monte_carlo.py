# -*- coding:utf-8 -*-
#######################################################################
# Copyright (C) 2016 Shijie Huang(harveyh@student.unimelb.edu.au)     #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################
from monte_carlo_class import *

# initialize parameters
S0 = 100.0  # e.g. spot price = 35
K = 100.0  # e.g. exercise price = 40
T = 1.0  # e.g. one year
mue = 0.05  # e.g. expected return of the asset, under risk neutral assumption, mue = r
r = 0.05  # e.g. risk free rate = 1%
sigma = 0.25  # e.g. volatility = 5%
div_yield = 0.0  # e.g. dividend yield = 1%
no_of_slice = 252  # no. of slices PER YEAR e.g. quarterly adjusted or 252 trading days adjusted

barrier_price = 80.0  # barrier level for barrier options
parisian_barrier_days = 21  # no.of consecutive trading days required for parisian options

# optional parameter
simulation_rounds = 100000  # For monte carlo simulation, a large number of simulations required

# initialize
MT = MonteCarloOptionPricing(S0=S0,
                             K=K,
                             T=T,
                             r=r,
                             mue=mue,
                             sigma=sigma,
                             div_yield=div_yield,
                             simulation_rounds=simulation_rounds,
                             no_of_slices=no_of_slice,
                             # fix_random_seed=True,
                             fix_random_seed=500)

# MT.vasicek_model()  # use vasicek model to simulate the interest rate
# MT.cox_ingersoll_ross_model()  # use Cox_Ingersoll_Ross model to simulate the interest rate
# MT.CIR_heston()  # CIR interest rate and Heston model to simulate volatility (sigma)

MT.stock_price_simulation()
# MT.stock_price_simulation_with_poisson_jump(jump_alpha=0.1, jump_std=0.25, poisson_lambda=0)
MT.european_call()
MT.asian_avg_price_option(avg_method='arithmetic', option_type="call")
MT.american_option_longstaff_schwartz(poly_degree=2, option_type="put")
MT.barrier_option(option_type="call",
                  barrier_price=barrier_price,
                  barrier_type="knock-in",
                  barrier_direction="down",
                  parisian_barrier_days=parisian_barrier_days)

MT.look_back_european()
