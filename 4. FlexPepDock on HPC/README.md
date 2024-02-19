# All files and dependencies to run FlexPepDock on LSU HPC SuperMIC.

## <ins>Software<ins>

Rosetta ver. 3.13  
PyMOL ver 2.3.3+

## <ins>Submission<ins>
1. "PreProcess.sub" - identifies all "ranked_0.pdb" files in the input folder and positions the structure in our modified PDB:1FCC file. "ranked_0.pdb" files are generated by AlphaFold2 and represent the predicted structure with the lowest lDDT. See Figure 1 for a visual description of this process.  
2. "prepack.sub" - runs the modified PDB files through Rosetta's prepacking step to remove internal residue clashes prior to docking. 
3. "flex_multinode.sub" - submission script for LSU HPC that takes the output directory from "prepack.sub" as input and runs FlexPepDock using the resulting files. 
4. "combinescore.py" - Python script that pulls specific output variables from FlexPepDock output files and compiles them into a single Excel file (.xlsx).

    #### <ins>PreProcess Dependencies<ins>  
   
    "COMPLEX_1fcc_truncated.pdb" - Modified PDB file of PDB:1FCC. This file is used to position the predicted structure of each GB1 variant along the IgG-Fc fragment structure prior to simulated docking. 

    "script.pml" - contains the commands for PyMOL to align each new GB1 variant structure to the original and delete the original structure. 

    #### <ins>Prepack Dependencies<ins>
    
    "prepack_flags" - contains flags for FlexPepDock prepack function which removes internal clashes within the protein prior to Refinement docking protocol.
    
    #### <ins>FlexPepDock Dependencies<ins>

    "flags" - contains flags for FlexPepDock to designate desired run specifications. See Rosetta documentation for full descriptions. 

    

