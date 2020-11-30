# importing the pysam package that enables the parsing of BAM files to python
import pysam 
#built-in method for calling the alignment file
samfile=pysam.AlignmentFile("<PATH>/filename.sorted")
# searches for the specified strings in the alignment
list=("chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21”,”chr22”,”chrX")
# employs the fetch method in a loop to call forth the unique and specific read mapping to a particular chromosome
for i in list:
    iter=samfile.fetch(i)
    print (str(i))
    count=0
    for x in iter:
        print (str(x))
        count+=1
        print (count)
#end
