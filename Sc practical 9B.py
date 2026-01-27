#Aim: Solve Tipping problem using fuzzy logic.
#install library(TWO)
#pip install scikit-fuzzy
#pip install numpy matplotlib
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality['poor'] = fuzz.trimf(quality.universe, [0, 0, 5])
quality['average'] = fuzz.trimf(quality.universe, [0, 5, 10])
quality['good'] = fuzz.trimf(quality.universe, [5, 10, 10])

service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trimf(service.universe, [0, 5, 10])
service['good'] = fuzz.trimf(service.universe, [5, 10, 10])

tip['less'] = fuzz.trimf(tip.universe, [0, 0, 10])
tip['some'] = fuzz.trimf(tip.universe, [5, 13, 20])
tip['much'] = fuzz.trimf(tip.universe, [15, 25, 25])

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['less'])
rule2 = ctrl.Rule(service['average'], tip['some'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['much'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = float(input("Enter food quality (0-10): "))
tipping.input['service'] = float(input("Enter service level (0-10): "))

tipping.compute()
print("Recommended tip:", round(tipping.output['tip'], 2))

quality.view()
service.view()
tip.view()
