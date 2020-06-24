import pickle

obj = [
    {'id':1, 'name':'Stuffy'},
    {'id':2, 'name': 'Fluffy'}
]

with open('file.p', 'wb') as f:
    pickle.dump(obj, f)

with open('file.p', 'rb') as f:
    loaded_obj = pickle.load(f)

print(loaded_obj) #=> [{'id': 1, 'name': 'Stuffy'}, {'id': 2, 'name': 'Fluffy'}]

