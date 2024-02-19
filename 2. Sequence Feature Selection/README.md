The "Sequence Feature Preparation.ipynb" Jupyter notebook was used to extract sequence encodings and/or learned embeddings from a master list ("onehot.csv", "georgiev.csv" or "msa_transformer_with_combo.csv"), generate library files that did not contain GB1 variants used in the training data ("LIBRARY_MINUS_LIST.csv"), and to pull the fitness scores of GB1 variants ("Fitness_List.csv").

Due to the file sizes of some of the input libraries, you can find all input library files used on our [Box](https://lsu.box.com/s/co98vz8qni9wfb583i0okbx8gkh6tfeh).

<ins>Optional Input Libraries<ins>

"msa_transformer_with_combo.csv" contains the 4-letter designation for each non-imputed GB1 variant in the first column and the corresponding MSA Transformer learned embedding in the subsequent columns. This file was modified from Wittmann et al. 2019 supplemental information [[Ref.]](https://www.cell.com/cell-systems/fulltext/S2405-4712(21)00286-6) to include the 4-letter designation for each GB1 variant in the first column.

"onehot.csv" and "georgiev.csv" contain the 4-letter designation for each non-imputed GB1 variant in the first column and the corresponding OneHot or Georgiev/AA-Index encoding in the subsequent columns, respectively.

"Fitness_List.csv" contains each non-imputed GB1 variant's 4-letter designation in the first column and the corresponding fitness score in the subsequent column. 


