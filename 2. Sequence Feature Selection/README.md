The "Sequence Feature Preparation.ipynb" Jupyter notebook was used to extract MSA Transformer learned embeddings from a master list ("msa_transformer_with_combo.csv"). This file was taken directly from Wittmann et al. 2019 supplemental information (https://www.cell.com/cell-systems/fulltext/S2405-4712(21)00286-6?). 

This notebook was also used to generate library files that did not contain GB1 variants used in the training data ("msa_transformer_with_combo_MINUS_LIST.csv") and was used to pull the fitness scores of GB1 variants (swap "msa_transformer_with_combo.csv" to "Fitness_List.csv"). 

"msa_transformer_with_combo.csv" is a dependecy file that contains each non-imputed GB1 variant's 4-letter designation in the first column and the corresponding MSA Transformer learned embedding in the subsequent columns. 

"Fitness_List.csv" is a dependency file that contains each non-imputed GB1 variant's 4-letter designation in the first column and the corresponding fitness score in the subsequent column. 


