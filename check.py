# importing the module
import json

def missing_clause(clause, test_clause):

	with open(clause) as f:
		data = f.read()
	js = json.loads(data)

	with open(test_clause) as f:
		data1 = f.read()
	test = json.loads(data1)

	for item in js:
		if item not in test:
			return item['clause_name']

# def missing_clause():
	
# 	for key in 

# 		    for key in dict1.keys():
#         if key not in dict2:
#             unique_pairs[key] = dict1[key]