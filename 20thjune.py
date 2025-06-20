# json file handling
import json
import numpy as np
x =  '{ "name":"Himasri", "age":21, "city":"Hyderabad"}'
y = json.loads(x)
print(y["age"])
a = { "name":"Pranathi", "age":20, "city":"Hyderabad"}
b = json.dumps(a)
print(b)
c = {
  "name": "Rashmitha",
  "age": 21,
  "married": False,
  "divorced": False,
  "children": ("RC","CR"),
  "pets": None,
  "cars": [
    {"model": "Honda", "mpg": 27.5},
    {"model": "Edge", "mpg": 24.1}
  ]
}
# print(json.dumps(c))
# print(json.dumps(c,indent=4))
print(json.dumps(c,indent=4, separators=(" "," = "), sort_keys=True))
# numpy matrix operations
np1 = np.random.randint(1,100,size=(2,2))
np2 = np.random.randint(1,100,size=(2,2))
print("np1, np2:  ", np1,np2, sep="#####")
print("matrixmul: ",np.matmul(np1,np2))
result = np.zeros((2,2))
print("result: ", result)
print("matrixmul: ",np.matmul(np1,np2, out = result))
print("norm of np1: ",np.linalg.norm(np1))
print("norm of np2 along x-axis", np.linalg.norm(np2, ord=1, axis=0)) #ord=1 is L1form which means just adding the absoulte values
print("norm of np2 along y-axis", np.linalg.norm(np2, axis=1))
print("trace of np1: ", np.trace(np1, offset=0))
print("trace of np1 with (-ve) offset: ", np.trace(np1, offset=-1))
print("trace of np1 with (+ve) offset: ", np.trace(np1, offset=1))
# probability and stats
# Bernoulli distribution: when we have only 2 outputs - either success/failure, used in binary classification
# Binomial Distribution: no.of sucesses in n indepentent trials, used in evaluation meterics, eg: how many heads when flipped coins 10 times
# Normal Distribution(Gaussian): bell shaped curve defined by mean and standard deviation
# mean: center data
# variance: how the data is spread across the mean. high var=>more spread out, low var=>closer to mean, Used in feature scaling (Standardization)
# evaluating model stability
# standard deviation: sqrt of var, used to normalise the data, find outliers
# skewness: measure of asymmetry of data, helps in understanding the  distribution



