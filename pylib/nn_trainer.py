# Based on https://towardsdatascience.com/inroduction-to-neural-networks-in-python-7e0b422e6c24

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import os
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split


from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score


class CSVDataAggregator:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.dataframes = []

    def _list_csv_files(self):
        csv_files = [f for f in os.listdir(self.folder_path) if f.endswith('.csv')]
        return csv_files

    def aggregate_data(self, debug):
        csv_files = self._list_csv_files()
        self.dataframes = []
        
        for file in csv_files:
            file_path = os.path.join(self.folder_path, file)
            df = pd.read_csv(file_path)
            self.dataframes.append(df)
        
        combined_data = pd.concat(self.dataframes, ignore_index=True)
        combined_data['magnitude'] = combined_data.apply(lambda row: np.sqrt(row['latitudeStdDev']**2 + row['longitudeStdDev']**2), axis=1)
        
        # print(type(combined_data))

        solType_replace_mapping = {'SINGLE':16, 
                                   'PSRDIFF':17, 
                                   'L1_FLOAT':32, 
                                   'NARROW_FLOAT':34, 
                                   'L1_INT':48, 
                                   'WIDE_INT':49, 
                                   'NARROW_INT':50, 
                                   'INS_PSRSP':52, 
                                   'INS_PSRDIFF':54, 
                                   'INS_RTKFLOAT':55, 
                                   'INS_RTKFIXED':56, 
                                   'PPP_CONVERGING':68, 
                                   'PPP':66, 
                                   'INS_PPP_CONVERGING':73, 
                                   'INS_PPP':74, 
                                   'PPP_BASIC_CONVERGING':77}
        
        solStatus_replace_mapping = {'SOL_COMPUTED':0,
                                     'INSUFFICIENT_OBS':1,
                                     'NO_CONVERGENCE':2,
                                     'SINGULARITY':3,
                                     'COV_TRACE':4,
                                     'TEST_DIST':5,
                                     'COLD_START':6,
                                     'V_H_LIMIT':7,
                                     'VARIANCE':8,
                                     'RESIDUALS':9,
                                     'INTEGRITY_WARNING':13,
                                     'PENDING':18,
                                     'INVALID_FIX':19,
                                     'UNAUTHORIZED':20,
                                     'INVALID_RATE':22}
        
        
        combined_data['solType'].replace(solType_replace_mapping, inplace=True)
        combined_data['solStatus'].replace(solStatus_replace_mapping, inplace=True)

        # DEBUG
        if debug == 'true':
            CSVExporter(combined_data, 'combined_data.csv')
        return combined_data
    
class CSVExporter:
    def __init__(self, data_to_csv, debug_filename):
            print('Saving cvs...')
            data_to_csv.to_csv(debug_filename, index=False)
            print('CVS Saved!')
    

class NeuralNetwork():
    def __init__(self, train_in, train_out):
        super(NeuralNetwork, self).__init__()
        model = Sequential()
        model.add(Dense(units=32, activation='relu', input_dim=len(train_in.columns)))
        model.add(Dense(units=64, activation='relu'))
        model.add(Dense(units=1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')
        model.fit(train_in, train_out, epochs=200, batch_size=32)

        return None

    def test_model(model, test_in, test_out):
        test_prediction = model.predict(test_in)
        accuracy_score(test_in, test_prediction)
        print(f'Accuracy score {accuracy_score}')

    def model_save(model, filename):
        model.save(filename)

##### Main Function #####
if __name__ == "__main__":

    # Grab data from folder
    training_data_folder = '/media/autobuntu/chonk/chonk/git_repos/Van_Gps_Study/DATA/'
    data_aggregator = CSVDataAggregator(training_data_folder)
    training_data = data_aggregator.aggregate_data(debug='true')

    # print(type(training_data))
    # print(training_data.head)
    # print(training_data.dtype.names)

    NN_Data_Inputs_ALL = training_data[['solutionAge', 'solStatus', 'numSatsTracked', 'numSatsInSolution', 'solType', 'numSatsL1', 'differentialAge']]
    NN_Data_Output_ALL = training_data[['magnitude']]

    NN_Train_Data_Inputs, NN_Test_Data_Inputs, NN_Train_Data_Outputs, NN_Test_Data_Outputs = train_test_split(NN_Data_Inputs_ALL, NN_Data_Output_ALL, test_size=0.2)
    
    # CSVExporter(NN_Train_Data_Inputs, 'NN_Train_Data_Inputs.csv')

    # print(NN_Train_Data_Inputs.head)
    # print(NN_Train_Data_Outputs.head)
    # print(NN_Test_Data_Inputs.head)
    # print(NN_Test_Data_Outputs.head)
    # print(len(NN_Train_Data_Inputs))
    # print(len(NN_Train_Data_Outputs))
    # print(len(NN_Test_Data_Inputs))
    # print(len(NN_Test_Data_Outputs))

    model = NeuralNetwork(NN_Train_Data_Inputs, NN_Train_Data_Outputs)

    model.test_model(NN_Test_Data_Inputs, NN_Test_Data_Outputs)

    model.save('tfmodel')


