library(dplyr)
library(readr)
library(ggpubr)
setwd("/path/to/working/directory/")
reference <- read_tsv("reference.txt")
sample <- read_tsv("sample.txt")
gencode_annotation_gtf <- rtracklayer::import("gencode.v36lift37.annotation.gtf")
gencode_annotation_gtf_1 <- as.data.frame(gencode_annotation_gtf)
width <- gencode_annotation_gtf_1[,4]
type <- gencode_annotation_gtf_1[,7]
gene_id <- gencode_annotation_gtf_1[,10]
gene_name <- gencode_annotation_gtf_1[,12]
original_annotation_required_cols <- data.frame(width,type,gene_id,gene_name)
reference_gene_name_matched <-left_join(reference,original_annotation_required_cols, by = c("Gene_name"= "gene_name"))
reference_gene_name_matched <- na.omit(reference_gene_name_matched)
reference_only_gene<- subset(reference_gene_name_matched, type == "gene")
reference_only_gene <- na.omit(reference_only_gene)
correlation_matrix <- left_join(reference_only_gene,sample, by = c("gene_id"="Gene_ID"))
correlation_matrix <- na.omit(correlation_matrix)
ggscatter(correlation_matrix, x = 'log2FC', y = 'log2FC', color = "blue", add = "reg.line",add.params = list(color = "black", fill = "lightgray"),conf.int = TRUE, cor.coef = TRUE, cor.method = "pearson", ylab = "log2FC Sample", xlab = "log2FC Reference", size = 0.5,rug = TRUE, title = "Correlation log2FC Sample Vs log2FC Reference")