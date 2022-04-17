import pickle
import sys

params = {'зарплата': 50000, 'bonus': 20000}

with open('params.pickle', 'wb') as f:
    pickle.dump(params, f)

with open('params.pickle', 'rb') as f:
    params = pickle.load(f)

print(params, type(params))

sys.exit(1)


