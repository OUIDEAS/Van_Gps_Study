# Based on https://towardsdatascience.com/inroduction-to-neural-networks-in-python-7e0b422e6c24

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import os

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

        # DEBUG
        if debug == 'true':
            print('Saving cvs...')
            debug_filename = f'debug_aggregated_data.csv'
            combined_data.to_csv(debug_filename, index=False)
            print('CVS Saved!')
        return combined_data.to_numpy()

# create NeuralNetwork class
class NeuralNetwork:

    # intialize variables in class
    def __init__(self, inputs, outputs, weights):
        self.inputs  = inputs
        self.outputs = outputs
        self.weights = weights
        self.error_history = []
        self.epoch_list = []

    #activation function ==> S(x) = 1/1+e^(-x)
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # going backwards through the network to update weights
    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # train the neural net for 25,000 iterations
    def train(self, epochs=25000):
        for epoch in range(epochs):
            # flow forward and produce an output
            self.feed_forward()
            # go back though the network to make corrections based on the output
            self.backpropagation()    
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    # function to predict output on new and unseen input data                               
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction



if __name__ == "__main__":

    # Grab data from folder
    training_data_folder = '/media/autobuntu/chonk/chonk/git_repos/Van_Gps_Study/DATA/'
    data_aggregator = CSVDataAggregator(training_data_folder)
    training_data = data_aggregator.aggregate_data(debug='true')

        
    # # create neural network   
    # NN = NeuralNetwork(inputs, outputs)
    # # train neural network
    # NN.train()

    # # create two new examples to predict                                   
    # example = np.array([[1, 1, 0]])
    # example_2 = np.array([[0, 1, 1]])

    # # print the predictions for both examples                                   
    # print(NN.predict(example), ' - Correct: ', example[0][0])
    # print(NN.predict(example_2), ' - Correct: ', example_2[0][0])

    # # plot the error over the entire training duration
    # plt.figure(figsize=(15,5))
    # plt.plot(NN.epoch_list, NN.error_history)
    # plt.xlabel('Epoch')
    # plt.ylabel('Error')
    # plt.show()