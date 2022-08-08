#Parse information from a file into different data structures, this piece of code specifically looks at files from the Saccharomyces Genome Database

import pandas as pd
SGD_features = pd.read_csv(/path/to/file/, sep = "\t")
SGD_Features_df = pd.DataFrame(SGD_features)
SGD_Features_df.columns = ['Primary SGDID', 'Feature type', 'Feature qualifier', 'Feature name','Standard gene name','Alias','Parent feature name','Secondary SGDID','Chromosome','Start_coordinate','Stop_coordinate','Strand','Genetic position','Coordinate version','Sequence version','Description'] 
SGD_Features_df.dropna(inplace = True)


#Creates a numpy array from Pandas dataframe column: The array data structure was chosen as the values here are of the same type - string
unique_feature_type = SGD_Features_df['Feature type'].unique()
print(unique_feature_type)


#Using a dictionary to represent feature types and feature names as key value pairs
dictionary = SGD_Features_df.set_index('Feature type')['Feature name'].T.to_dict()
print(dictionary)

for i in SGD_Features_df.index:
     print(SGD_Features_df['Feature type'][i], SGD_Features_df['Feature name'][i])

coordinates = pd.Series(SGD_Features_df.Start_coordinate.values,index=SGD_Features_df.Stop_coordinate).to_dict()
print(coordinates)