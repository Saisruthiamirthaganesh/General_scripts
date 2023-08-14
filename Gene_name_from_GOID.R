library(biomaRt)
load data from file to dataframe
go_terms = read.table("gene_list.txt", sep = '\t')
ensembl = useMart("ensembl",dataset="hsapiens_gene_ensembl")
gene.data <- getBM(attributes=c('hgnc_symbol', 'ensembl_transcript_id', 'go'),filters = 'go', values = go_terms, mart = ensembl)
unique(gene.data$hgnc_symbol)
length(unique(gene.data$hgnc_symbol))
write.table(genes, "learning.txt", quote = FALSE, row.names = FALSE, col.names = FALSE)

