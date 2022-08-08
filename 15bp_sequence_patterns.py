#Script to get the top 10 commonly occurring sequences based on the first 15bp
from Bio import SeqIO
from pathlib import Path
import collections
import itertools


#Set path to file


data_folder = Path("/path/to/folder/")
file_to_open = data_folder / "filename.fq"


sequences = []


#Using SeqIO from biopython to import fastq as a SeqRecord


with open(file_to_open) as handle:
    for record in SeqIO.parse(handle, "fastq"):
        sequences.append(record.seq[0:15]) #Appending the first 15 bases of each sequence as a list element to sequences


# Getting the counts for each matching string in the list as a dictionary item with the sequence being the key and the counts being the value


my_dict = {i:sequences.count(i) for i in sequences}


#Sorting the dictionary in the descending order to get the top 10 results with highest counts


sorted_dict = sorted(my_dict.items(), key=lambda kv: kv[1],reverse=True)
top_sequences = collections.OrderedDict(sorted_dict)
N=10
out = dict(itertools.islice(top_sequences.items(), N)) 
print("The most commonly occurring start sequences are: ", out)
