input_file="ENCFF134CQC"
./bigBedToBed $input_file.bigBed $input_file.bed
./bedClip $input_file.bed ../mm10.chrom.sizes $input_file.clip.bed
cut -f1,2,3,5 $input_file.clip.bed | sort -k1,1 -k2,2n > $input_file.sorted.bedGraph
cat $input_file.sorted.bedGraph | awk -F '\t' -v OFS='\t' '{print $1,$2,$3-1,$4}' > $input_file.sorted.bedGraph.tmp1
bedtools merge -i $input_file.sorted.bedGraph.tmp1 -c 4 -o mean > $input_file.sorted.bedGraph.M.tmp1
cat $input_file.sorted.bedGraph.M.tmp1 | awk -F '\t' -v OFS='\t' '{print $1,$2,$3+1,$4}' > $input_file.bedGraph
./bedGraphToBigWig $input_file.bedGraph ../mm10.chrom.sizes $input_file.sorted.bw
cut -f1,2,3,4 $input_file.clip.bed | sort -k1,1 -k2,2n > $input_file.nopkname.bed
cat $input_file.nopkname.bed | awk -F '\t' -v OFS='\t' '{print $1, $2, $3, $1"_"$2"_"$3}' > $input_file.withpkname.bed
sort $input_file.withpkname.bed | uniq > $input_file.withpkname.uniq.bed
./bigWigAverageOverBed $input_file.sorted.bw $input_file.withpkname.uniq.bed $input_file.bigbedfile1.tab
sort -k1,1 $input_file.bigbedfile1.tab > $input_file.bigbedfile1.pkidsort.tab




cat CFUE/ENCFF134CQC/ENCFF134CQC.clip.bed CFUE/ENCFF599ZDJ/ENCFF599ZDJ.clip.bed erythroblast/ENCFF181AMY/ENCFF181AMY.clip.bed erythroblast/ENCFF616EWK/ENCFF616EWK.clip.bed | sort -k1,1 -k2,2n > all_peaks.merged.bed
cat all_peaks.merged.bed | awk -F '\t' -v OFS='\t' '{print $1,$2,$3,$1"_"$2"_"$3}' > master_peak_list.withpkname.bed
sort master_peak_list.withpkname.bed | uniq > master_peak_list.uniq.bed
./bigWigAverageOverBed ../CFUE/ENCFF134CQC/ENCFF134CQC.sorted.bw ../master_peak_list.uniq.bed ENCFF134CQC.final.tab
sort -k1,1 ENCFF134CQC.final.tab > ENCFF134CQC.pkidsort.tab
cut -f1,6 ENCFF134CQC.pkidsort.tab > ENCFF134CQC.de.tsv
