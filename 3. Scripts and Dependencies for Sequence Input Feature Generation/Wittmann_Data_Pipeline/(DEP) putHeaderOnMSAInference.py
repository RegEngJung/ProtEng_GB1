# PREVIOUS WORK IN PROGRESS SCRIPT USED TO PUT A HEADER ON THE MSA TRANSFORMER FILE
# NOT USED, USE inference_remove_rehead.py INSTEAD

import pandas as pd 
import csv 
# move to test_inference_creator_msa.py
inference = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training.csv"
output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training_with_proper_headings.csv"
columnNames= []
df = pd.read_csv(inference, header = None)
for column,k in (enumerate(df)):
	columnNames.append(f"msa{k}")
columnNames[0] = 'id'
df.columns = columnNames
print(df.head())
df.to_csv(output_, index =False)