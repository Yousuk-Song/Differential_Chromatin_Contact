library(edgeR)
library(pheatmap)
library(Rtsne)
library(ggplot2)

# 데이터 로드
data_file <- "/Users/song-yuseog/Desktop/R_script/K562_DCI/SRR1658693.Chromatin_Contact.Normal-Philadelphia.merged.csv"

# CSV 파일을 읽어 edgeR 데이터 객체로 변환.
data <- read.csv(data_file, header = TRUE, row.names = 1)

# edgeR 데이터 객체 생성.
dge <- DGEList(counts = data)

# 데이터 정규화
dge <- calcNormFactors(dge)

# 분산-평균 기반 가중치 계산 수행.
dge <- estimateCommonDisp(dge)

# 유전자 발현 분석 수행.
dge <- estimateTagwiseDisp(dge)

# heatmap 생성 

sample_groups <- c("Normal", "Philadelphia")

ann_col <- data.frame(type = as.factor(sample_groups)) # sample의 type  나타내기


# Heatmap 그리기 
heat <- pheatmap(dge, 
                 border_color = NA, 
                 cluster_rows = TRUE,
                 cluster_cols = FALSE, 
                 main = "Differential Chromatin Interaction: Normal vs Philadelphia chromosome",
                 fontsize_row = 10, 
                 color = colorRampPalette(c("forestgreen", "black", "red"))(100),
                 width = 1, angle_col = 315)

png(filename = "/Users/song-yuseog/Desktop/R_script/K562_DCI/DCI_N_vs_P.heatmap.png", width = 600, height = 960) # 파일 이름과 크기 지정
print(heat) # heatmap 그리기
dev.off() # 출력 종료



# 피셔 exact test로 유의하게 차이나는 gene 뽑기 --> 2개 이상의 샘플로 구성된 그룹 있어야함 
# edgeR를 사용하여 유의한 유전자 식별
dge <- exactTest(dge)

# 유의한 유전자를 선택하기 위한 조건 설정 (예: FDR < 0.05, 로그 폴드 차이 > 4)
significant_genes <- topTags(dge, n = nrow(dge), sort.by = "p.value")$genes
significant_genes <- significant_genes[significant_genes$FDR < 0.05 & abs(significant_genes$logFC) > 4, ]

# 유의한 유전자 목록 출력
write.csv(significant_genes, file = "/Users/song-yuseog/Desktop/R_script/K562_DCI/significant_genes.csv")

# 유의한 유전자의 수 출력
cat("Number of significant genes:", nrow(significant_genes), "\n")
