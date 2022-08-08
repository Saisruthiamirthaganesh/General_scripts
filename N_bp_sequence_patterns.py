from itertools import *
file_to_open = "reads.fq"

def header(line):
  return not (line.startswith("@") or line.startswith("+"))

sequences = []
kmers =[]
kmer_abundance ={}
        
def Counter(N,k):
    if N>k :
        with open(file_to_open) as stream:
            stream = filter(header, stream)
            stream = islice(stream,0,None,2)
            for line in stream:
                sequences.append(line[0:N])
                
            for k in range(N):
                for line in sequences:
                    kmers.append(line[0:k])
                    unique_count = {kmers.count(i) for i in kmers}
	    for i in kmers:
		if i in kmer_abundance:
		    kmer_abundance[i] +=1
		else:
		    kmer_abundance[i] = 1		
    else:
        print("Error: The N value is smaller than k-mer length")
    sorted_dict = sorted(kmer_abundance.items(), key=lambda kv: kv[1],reverse=True)
    top_sequences = collections.OrderedDict(sorted_dict)
    N=10
    out = dict(itertools.islice(top_sequences.items(), N)) 
    print("The most commonly occurring start sequences are: ", out)
    
    return unique_count

#Function call
print(Counter(10,3))
