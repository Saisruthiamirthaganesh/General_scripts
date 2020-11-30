library(readr)
library(rtracklayer)
library(tidyr)
library(tidyverse)
library(plyr)
#setwd("") #set the path to the current working directory
targeted_genes_transcripts <- read_tsv("targeted_genes_transcripts.txt")
gtf_annotation <- rtracklayer::import("/data/Priyanka/other_pipelines/iCOMIC/benchmarking_RNA/Ensembel_GRCh37_75/Homo_sapiens.GRCh37.75.gtf")
gtf_annotation_1 <- as.data.frame(gtf_annotation)
targeted_transcripts <- separate_rows(targeted_genes_transcripts, transcript_id, sep = ",")
filtered_genes <- match_df(gtf_annotation_1,targeted_genes_transcripts, on = "gene_id")
filtered_only_genes <- filtered_genes[filtered_genes$type == 'gene',]
filtered_final <- match_df(filtered_genes,targeted_genes_transcripts, on = "transcript_id")
printed_gene <- 'test'
#by(filtered_final, 1:nrow(filtered_final), function(row){
for (row_index in 1:nrow(filtered_final)) {
    row <- filtered_final[row_index,]
  #if(row[7] == "transcript"){
    #print(row[[7]])
    #print(gene)
    #print(printed_gene)
    if(printed_gene != row[[10]]){
    gene <- filtered_only_genes[filtered_only_genes$gene_id == row[[10]],]
    gtf_manipulated <- paste(gene[[1]],gene[[6]],gene[[7]],gene[[2]],gene[[3]],
                             gene[[8]],gene[[5]],gene[[9]],sep="\t")
    gtf <- gtf_manipulated %>% paste("\tgene_id \"", gene[[10]], "\"; gene_name \"", gene[[11]], 
                                     "\"; gene_source \"", gene[[12]], "\"; gene_biotype \"", gene[[13]], 
                                     "\"; transcript_id \"", gene[[14]], "\"; transcript_name \"", gene[[15]], 
                                     "\"; transcript_source \"", gene[[16]], "\"; exon_number \"", gene[[17]], 
                                     "\"; exon_id \"", gene[[18]], "\"; tag \"", gene[[19]], 
                                     "\"; ccds_id \"", gene[[20]], "\"; protein_id \"", gene[[21]], "\"", sep="")
    write.table(gtf, "Annotation_new_qpcr5.gtf", col.names = FALSE, quote = FALSE, row.names = FALSE, append = TRUE)    
    }
    printed_gene <- row[[10]]
    gtf_manipulated <- paste(row[[1]],row[[6]],row[[7]],row[[2]],row[[3]],
                             row[[8]],row[[5]],row[[9]],sep="\t")
    gtf <- gtf_manipulated %>% paste("\tgene_id \"", row[[10]], "\"; gene_name \"", row[[11]], 
                                     "\"; gene_source \"", row[[12]], "\"; gene_biotype \"", row[[13]], 
                                     "\"; transcript_id \"", row[[14]], "\"; transcript_name \"", row[[15]], 
                                     "\"; transcript_source \"", row[[16]], "\"; exon_number \"", row[[17]], 
                                     "\"; exon_id \"", row[[18]], "\"; tag \"", row[[19]], 
                                     "\"; ccds_id \"", row[[20]], "\"; protein_id \"", row[[21]], "\"", sep="")
    #print(gtf)
    write.table(gtf, "Annotation_new_qpcr5.gtf", col.names = FALSE, quote = FALSE, row.names = FALSE, append = TRUE)
    #break
#  }
}
#gtf_manipulated <- filtered_final[,c(1,6,7,2,3,8,5,9)]
#gtf_cols <- gtf_annotation[,8:13]
#gtf_manipulated %>% paste(gtf_cols, sep = "/" , collapse = ";")


#gtf <- gtf_manipulated %>% paste("\tgene_id \"", row[[10]], "\"; gene_name \"", row[[11]], 
#                                 "\"; gene_source \"", row[[12]], "\"; gene_biotype \"", row[[13]], 
#                                 "\"; transcript_id \"", row[[14]], "\"; transcript_name \"", row[[15]], 
#                                 "\"; transcript_source \"", row[[16]], "\"; tag \"", row[[19]], 
#                                 "\"; ccds_id \"", row[[20]], "\"", sep="")