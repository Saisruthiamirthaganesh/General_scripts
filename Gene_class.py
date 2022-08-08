#Create a class to represent a Gene

#Create class
class Gene:
#Creating a constructor to initialise      
    def __init__(self, transcripts,identifier, gene_name, expression_level):
        self.transcripts=[]
        self.identifier = identifier
        self.gene_name = gene_name
        self.expression_level = expression_level
        


# Creating a function to print the details of the genes
    def describe(self):
            print("The official gene ID is:",self.identifier)
            print("Gene name:",self.gene_name)
            print("The expression level for the above gene is:",self.expression_level)


#Creating a function to add the expression levels if gene names are similar        
    def add(self,RNA):
        self.RNA=RNA
        for i in range(len(self.transcripts)):
             if self.gene_name==RNA.gene_name:
                 total = self.expression_level+self.RNA.expression_level
                 print(total)
             else :
                 print("Error: Gene names are different")


#Creating a function to compare the expression levels of two genes                 
    def compare(self,RNA):
        self.RNA = RNA
        if self.gene_name==RNA.gene_name:
            print("Gene names are the same, choose a different gene")
        else:
            for i in range(len(self.transcripts)):
                if self.expression_level>RNA.expression_level:
                    print("The expression of the first gene",self.gene_name,"is greater than that of the second gene",RNA.gene_name)
                else:
                    print("The expression of the second gene",RNA.gene_name,"is greater than that of the first gene",self.gene_name)


#Creating a function to see if the expression levels are similar between two genes               
    def similarity(self,RNA):
        self.RNA = RNA
        for i in range(len(self.transcripts)):
             if self.identifier==RNA.identifier and self.expression_level - RNA.expression_level<0.1:
                 print("Gene expression is similar for the genes",self.gene_name,"and",RNA.gene_name)
             else:
                 print("Gene expression is different for the genes",self.gene_name,"and",RNA.gene_name)
                 
#Creating objects and instances of the class                 
                 
RNA1 = Gene(1,"NC_013668","HBB2",40)
RNA2 = Gene(2,"NC_013668","HBB2",40.01)
RNA3 = Gene(3,'NC_02222','ASMT', 7)
RNA4 = Gene(4,"NC_04512",'BCL3',16)
RNA1.transcripts.append(1)
RNA2.transcripts.append(2)
RNA3.transcripts.append(3)
RNA4.transcripts.append(4)


#Calling functions of the class Gene
RNA1.describe()
RNA2.describe()
RNA3.describe()
RNA4.describe()




RNA2.add(RNA3)
RNA3.add(RNA4)
RNA4.add(RNA1)
RNA1.add(RNA2)


RNA1.compare(RNA2)
RNA2.compare(RNA3)
RNA3.similarity(RNA4)
RNA1.similarity(RNA2)