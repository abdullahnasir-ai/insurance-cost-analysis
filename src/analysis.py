from src.file_reader import data_list

age = [data['age'] for data in data_list]
sex = [data['sex'] for data in data_list]
bmi = [data['bmi'] for data in data_list]
num_of_children = [data['children'] for data in data_list]
smoker = [data['smoker'] for data in data_list]
region = [data['region'] for data in data_list]
insurance_cost = [data['charges'] for data in data_list]

