input_file=""
./bigBedToBed $input_file.bigBed $input_file.bed
./bedClip $input_file.bed ../mm10.chrom.sizes $input_file.clip.bed
cut -f1,2,3,5 $input_file.clip.bed | sort -k1,1 -k2,2n > $input_file.sorted.bedGraph
cat $input_file.sorted.bedGraph | awk -F '\t' -v OFS='\t' '{print $1,$2,$3-1,$4}' > $input_file.sorted.bedGraph.tmp1
bedtools merge -i $input_file.sorted.bedGraph.tmp1 -c 4 -o mean > $input_file.sorted.bedGraph.M.tmp1
cat $input_file.sorted.bedGraph.M.tmp1 | awk -F '\t' -v OFS='\t' '{print $1,$2,$3+1,$4}' > $input_file.bedGraph
./bedGraphToBigWig $input_file.bedGraph ../mm10.chrom.sizes $input_file.sorted.bw

cat ../CMP/ENCFF343PTQ/ENCFF343PTQ.clip.bed ../CMP/ENCFF832UUS/ENCFF832UUS.clip.bed ../HSC/ENCFF255IVU/ENCFF255IVU.clip.bed ../HSC/ENCFF662DYG/ENCFF662DYG.clip.bed ../CFUE/ENCFF599ZDJ/ENCFF599ZDJ.clip.bed ../CFUE/ENCFF796ZSB/ENCFF796ZSB.clip.bed ../erythroblast/ENCFF181AMY/ENCFF181AMY.clip.bed ../erythroblast/ENCFF616EWK/ENCFF616EWK.clip.bed | sort -k1,1 -k2,2n > all_peaks.merged.bed
cat all_peaks.merged.bed | awk -F '\t' -v OFS='\t' '{print $1,$2,$3,$1"_"$2"_"$3}' > master_peak_list.withpkname.bed
sort master_peak_list.withpkname.bed | uniq > master_peak_list.uniq.bed

inputfile=""
./bigWigAverageOverBed $inputfile.sorted.bw /storage/home/sma6401/work/statgenomics/all/master_peak_list.uniq.bed $inputfile.final.tab
sort -k1,1 $inputfile.final.tab > $inputfile.pkidsort.tab
cut -f1,6 $inputfile.pkidsort.tab > $inputfile.de.tsv
