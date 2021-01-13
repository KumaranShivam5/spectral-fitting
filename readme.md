
# Data generation
    data_gen_v2.py
 - Range of parameters and the energy bins can be edited in the source code itself
 - create a directory named 'data'
 - set the range of values and run data_gen_v2.py
 - generate two csv files
        data_spectrum.csv
        params_spectrum.csv
#### Dependencies
    soxs
    numpy
    matplotlib
    seaborn
# regression network training 
    regression.ipynb
 - uses the above generated data and parameter csv files
 - This is a jupyter notebook , every cell has a corresponding explanation
 - Run each cell in sequence
 - in the last cell the best model is generated, compiled and is stored as 
    fcc_model
# DAE/AE
    den_auto_encoder.ipynb
    auto_encoder_v_final.ipynb
 - In these notebooks the reconstructionand prediction is well implemented
 - Each cell is given with explanation in the notebook itself
 - Run each cell in sequential order.

 