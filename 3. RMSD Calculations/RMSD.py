# Script designed to sequentially load .pdb files predicted from AlphaFold2, 
# align them to a reference structure, and calculate RMSD within PyMOL. 
# Written by Jason Li, LSU HPC. 

from pymol import cmd
import os,sys

# I/O file path
ipath = sys.argv[1] if len(sys.argv)>1 else '.'
opath = sys.argv[2] if len(sys.argv)>2 else '.'
print("Search for 'ranked_0.pdb' files under '" + ipath + "'")

# Load fixed structure
cmd.load("1pga.pdb", "FIX")

# Open file and write
with open(opath+"/RMSD.csv", "w") as f:

    # Print header
    f.write("File,RMSD\n")
    
    # Find all ranked_0.pdb
    findranked0 = os.popen("find " + ipath + " -name ranked_0.pdb")
    for fpath in findranked0:
        
        # Find file name
        fname = fpath.strip().split("/")[-2]

        # Load found structure
        cmd.load(fpath.strip(), fname)

        # Align
        res = cmd.align(fname, "FIX", cycles=5, cutoff=2.0, mobile_state=-1, target_state=-1)
        print(res)   # I print the results out in case you need 

        # Print to output file
        f.write(fname + "," + str(res[0]) + "\n")
