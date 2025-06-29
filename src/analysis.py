from src.file_reader import data_list

age = [data['age'] for data in data_list]
sex = [data['sex'] for data in data_list]
bmi = [data['bmi'] for data in data_list]
num_of_children = [data['children'] for data in data_list]
smoker = [data['smoker'] for data in data_list]
region = [data['region'] for data in data_list]
insurance_cost = [data['charges'] for data in data_list]

def smoker_cost(smoker, insurance_cost):
    smoker_total = 0
    non_smoker_total = 0
    for i in range(len(smoker)):
        if smoker[i] == 'yes':
            smoker_total += insurance_cost[i]
        else:
            non_smoker_total += insurance_cost[i]
    average_smoker_cost = smoker_total / len(smoker)
    average_non_smoker_cost = non_smoker_total / len(smoker)
    return (f"The average cost for a smoker is {average_smoker_cost}, whereas the average cost for a non-smoker is {average_non_smoker_cost}")

def children_cost(num_of_children, insurance_cost):
    total_cost_child = {}
    for i in range(len(num_of_children)):
        key = int(num_of_children[i])
        if key not in total_cost_child:
            total_cost_child[key] = 0
        total_cost_child[key] += float(insurance_cost[i])
    final_string = ""
    for key, value in total_cost_child.items():
        count = num_of_children.count((str(key)))
        if count > 0:
            final_string += f"For Individuals with {key} children the average cost of insurance is {(value / count):.2f}. \n"
    return final_string






