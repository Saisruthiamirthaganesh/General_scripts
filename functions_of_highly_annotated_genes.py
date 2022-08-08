# Download Gene Ontology data
wget filename.gaf.gz
gunzip filename.gaf.gz


# Remove GAF header lines
sed '1,23d' filename.gaf > filename_no_header.gaf

# Remove the empty column present in the gaf file
# Import required packages
import pandas as pd
import collections

def create_dict(f):
    
    # Create dictionary with gene names/object names as key and the corresponding GO ID as values and sort the dictionary
    D=dict(zip(f.DB_Object_Name,f.GO_ID))
    sorted_dict=sorted(D.items(), key = lambda item: item[1], reverse=False)
    sorted_dict_anno= collections.OrderedDict(sorted_dict)
    return sorted_dict_anno
    
def grouping(dictionary):    
    # Grouping dataframe based on object name and getting unique count value for each entry - top 10 entries with highest values
    P=f.groupby('DB_Object_Name').count()
    sorted_p =P.sort_values(by = 'GO_ID',ascending=False)[:10]
    print(sorted_p)

    
def sorted_genes(dictionary):
# Creating a list from the top 10 entries identified in the previous step
    gene_list = ['List element 1','List element 2','List element 3',"List element 4","List element 5"]

    # Printing key value pairs corresponding to the object names
    for key,value in dictionary.items():
        for i in gene_list:
            if key == i:
                print(key)
                print(value)


# Read file with appropriate delimiter
f=pd.read_csv("filename_no_header.gaf",sep = "\t")
# Assign column names
f.set_axis(["DB","DB_Object_ID","DB_Object_Symbol","Qualifier","GO_ID","DB:Reference","With(or)_From","Evidence_Code","Aspect","DB_Object_Name","DB_Object_Type","Taxon","Assigned_By"],axis=1,inplace=True)
c=create_dict(f)
g=grouping(c)
sorted_genes(c)
