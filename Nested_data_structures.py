#Demonstration of building a nested data structure
#Types of data structures used: List, dictionary and dataframe


import pandas as pd
common_names = ["African Wild Dog","Amur Leopard","Arctic Fox","Black Rhino","Blue Whale","Giant Panda","Jaguar"]
scientific_names = ("Lycaon pictus","Panthera pardus orientalis","Vulpes lagopus","Diceros bicornis","Balaenoptera musculus","Ailuropoda melanoleuca","Panthera onca")
priority_rank = [2,1,5,1,2,3,4]


Animals = {common_names[i]: scientific_names[i] for i in range(len(common_names))}
print("Wildlife:",Animals)

Wildlife_index = pd.DataFrame.from_dict(Animals,orient='index')
Wildlife_index.columns = ["Scientific name"]
Wildlife_index.insert(1, "Priority rank", priority_rank, True)
print(Wildlife_index)

#Accessing the first item in the dataframe nested three levels deep

print(Wildlife_index.iloc[1])