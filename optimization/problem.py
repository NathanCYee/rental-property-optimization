import numpy as np
import tensorflow as tf
import random
from keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import json
from keras import backend as K
from platypus import NSGAII, Problem, Real


def predict(x, rent_model, sale_model):
    # Put in proper format to use in model
    inputs = [x]
    rent_price = rent_model.predict(inputs)
    sale_price = sale_model.predict(inputs)

    return rent_price[0], sale_price[0]


class RentSale(Problem):
    def __init__(self, rent_model, sale_model):
        super(RentSale, self).__init__(5, 2, 2)
        self.types[:] = [Real(100, 5000), Real(1, 8), Real(
            1, 8), Real(11368, 230952), Real(1, 143683.0)]
        self.constraints[:] = ">=0"
        self.rent_model = rent_model
        self.sale_model = sale_model

    def evaluate(self, solution):
        x = [
            solution.variables[0], #sqfeet
            round(solution.variables[1]), # bed
            round(solution.variables[2]), # bath
            solution.variables[3], # income
            solution.variables[4] # population density
        ]
        rent, sale = predict(x, self.rent_model, self.sale_model)
        # negate rent b/c we are trying to maximize
        solution.objectives[:] = [-rent, sale]
        # constrain so that there is a minimum ratio of 3 bedrooms per bathroom
        bed_bath_ratio = round(solution.variables[2])*3-round(solution.variables[1])
        # constrain so that every bedroom has 100 sq ft and every bathroom has 50 sq ft
        space_constraint = solution.variables[0]-(round(solution.variables[1])*150+round(solution.variables[2])*50+200)
        solution.constraints[:] = [bed_bath_ratio,space_constraint] 

class TBE(Problem):
    def __init__(self, rent_model, sale_model):
        super(TBE, self).__init__(5, 1, 2)
        self.types[:] = [Real(100, 5000), Real(1, 8), Real(
            1, 8), Real(11368, 230952), Real(1, 143683.0)]
        self.constraints[:] = ">=0"
        self.rent_model = rent_model
        self.sale_model = sale_model

    def evaluate(self, solution):
        x = [
            solution.variables[0], #sqfeet
            round(solution.variables[1]), # bed
            round(solution.variables[2]), # bath
            solution.variables[3], # income
            solution.variables[4] # population density
        ]
        rent, sale = predict(x, self.rent_model, self.sale_model)
        # negate rent b/c we are trying to maximize
        solution.objectives[:] = [sale/rent]
        # constrain so that there is a minimum ratio of 3 bedrooms per bathroom
        bed_bath_ratio = round(solution.variables[2])*3-round(solution.variables[1])
        # constrain so that every bedroom has 100 sq ft and every bathroom has 50 sq ft
        space_constraint = solution.variables[0]-(round(solution.variables[1])*100+round(solution.variables[2])*50)
        solution.constraints[:] = [bed_bath_ratio,space_constraint] 

class RentSaleTBE(Problem):
    def __init__(self, rent_model, sale_model):
        super(RentSaleTBE, self).__init__(5, 3, 2)
        self.types[:] = [Real(100, 5000), Real(1, 8), Real(
            1, 8), Real(11368, 230952), Real(1, 143683.0)]
        self.constraints[:] = ">=0"
        self.rent_model = rent_model
        self.sale_model = sale_model

    def evaluate(self, solution):
        x = [
            solution.variables[0], #sqfeet
            round(solution.variables[1]), # bed
            round(solution.variables[2]), # bath
            solution.variables[3], # income
            solution.variables[4] # population density
        ]
        rent, sale = predict(x, self.rent_model, self.sale_model)
        # negate rent b/c we are trying to maximize
        solution.objectives[:] = [-rent, sale, sale/rent]
        # constrain so that there is a minimum ratio of 3 bedrooms per bathroom
        bed_bath_ratio = round(solution.variables[2])*3-round(solution.variables[1])
        # constrain so that every bedroom has 100 sq ft and every bathroom has 50 sq ft
        space_constraint = solution.variables[0]-(round(solution.variables[1])*100+round(solution.variables[2])*50)
        solution.constraints[:] = [bed_bath_ratio,space_constraint] 