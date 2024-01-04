## Real-time Credit Card Fraud Detection System using Verilog and Basys 3

The project aims to enhance security in online financial transactions, particularly in credit card transactions, by leveraging both Machine Learning (ML) and Hardware Descriptive Languages (HDL) on the Basys 3 FPGA platform. 
FPGAs offer flexibility and reprogrammability, making them ideal for real-time fraud detection. 
The project combines ML algorithms for identifying fraudulent behavior with HDL on Basys 3 FPGA to accelerate computation tasks, ensuring efficient execution of the ML models. 

### Model Training

The first stage of this project was to develop a robust machine learning model to identify fraud correctly. For this task, the Kaggle dataset Credit Card Fraud was used. The dataset contained 1,000,000 data points. 800,000 were used for model training, and the remaining 200,000 for testing.

The important concern of the dataset is that it is highly skewed, with only 87,403 data points having the label ‘Fraud’.

A 3-layer Dense Neural network was trained with a sigmoid output at the end for fraud prediction.

The details are as follows
- The model was trained with Tensorflow
- Seven input features
  - Distance_from_home
  - Distance_from_last_transaction
  - Ratio_to_median_purchase_price
  - Repeat_retailer
  - Used_chip
  - Used_pin_number
  - online_order
- Layer 1 - 16 neurons with relu activation
- Layer 2 - 4 neurons with relu activation
- Layer 3 - 1 neuron with sigmoid activation
- Loss function - Binary cross entropy
- Optimizer- Adam with a 0.001 learning rate
- Trained for five epochs with a batch size of 16


### FPGA Implementation

The developed model needed to be deployed on the FPGA. For this purpose, we created the neural network architecture in Verilog and loaded the weights of the trained model. 
This paved the way for direct and real-time inference in the FPGA. 

The Neuron, Layer, and model were implemented as modules in the FPGA. 
Layers consisted of the relevant number of neurons, and the model contained the relevant layers. 
The connections between layers, inputs and outputs were also configured in Verilog.

The impelemented Network was tested by simulations and deployed on a Basys 3 FPGA.

