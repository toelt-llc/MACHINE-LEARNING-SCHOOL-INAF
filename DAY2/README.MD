# Deep Learning Module (HSLU CAS ML2)

Following hands-on are useful to the student.

Especially interesting are the following notebooks that can be opened directly in Google Colab for testing.

- Linear regression with one neuron [http://adl.toelt.ai/single_neuron/Linear_regression_with_one_neuron.html](http://adl.toelt.ai/single_neuron/Linear_regression_with_one_neuron.html)
- Logistic regression with one neuron [http://adl.toelt.ai/single_neuron/Logistic_regression_with_one_neuron.html](http://adl.toelt.ai/single_neuron/Logistic_regression_with_one_neuron.html)
- Multiclass classification with neural networks [http://adl.toelt.ai/FFNN/Multiclass_classification_with_fully_connected_networks.html](http://adl.toelt.ai/FFNN/Multiclass_classification_with_fully_connected_networks.html)

Also play with the [TensorFlow neural network playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.71013&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

## Hands-on exercises
### 1. First fully-connected neural network with Keras
This notebook trains a simple neural network on the MNIST dataset.

Network architecture
- How many hidden layers, how many neurons, what is the activation function?
- Verify with `model.summary()`
- Reduce the size of the hidden layer and retrain the model... what do you notice?

### 2. First example of a CNN
This notebook trains a simple CNN on the CIFAR-10 image classification challenge.

#### Part 1: Understanding the Model
1. Inspect the Architecture:
 - Execute model.summary() to get a detailed view of the model architecture.
 - How many convolutional layers are there? What is the role of each layer?

2. Initial Training:
 - Train the model for 10 epochs using the provided training data (x_train, y_train).
 - Check the accuracy on the test set using `model.evaluate(x_test, y_test)`. What is the initial accuracy?

3. Visualize Training:
 - Plot the training and validation loss over epochs using the provided code.
 - What can you infer from the loss curves? Is the model overfitting or underfitting?

#### Part 2: Experimenting with Hyperparameters
1. Modify Dropout Rate:
 - Change the dropout rates in the model (e.g., from 0.4 to 0.3).
 - Retrain the model for 10 epochs and visualize the training process.
- How does modifying the dropout rate impact the training and validation loss?

2. Adjust Learning Rate:
 - Change the learning rate in the optimizer (e.g., use `tf.keras.optimizers.Adam(lr=0.0001)`).
 - Retrain the model for 10 epochs and visualize the training process.
 - What changes do you observe in the loss curves?

#### Part 3: Improving the model
1. Experiment with Model Size:
 - Try increasing or decreasing the number of filters in convolutional layers or changing the size of the dense layer.
 - Retrain the model for 10 epochs and visualize the training process.
 - Did the model performance improve?

### 3. Real-world classification task
The SVHN dataset contains images of house numbers collected from Google Street View. Your task is to train a convolutional neural network to classify images from the SVHN dataset.

#### Steps:

1. **Load the SVHN Dataset:**
   - Obtain the SVHN dataset from https://www.kaggle.com/datasets/sasha18/street-view-house-nos-h5-file/
   - Extract the .h5 file from inside the archive
   - Load the dataset using
  ```
  with h5py.File('SVHN_single_grey1.h5', 'r') as file:
    x_train = np.array(file['X_train'])
    y_train = np.array(file['y_train'])
    x_test = np.array(file['X_test'])
    y_test = np.array(file['y_test'])
    x_val = np.array(file['X_val'])
    y_val = np.array(file['y_val'])
  ```
   - Explore the dataset to understand its structure.

2. **Preprocess the Data:**
   - Normalize the pixel values of the images to the range [0, 1].
   - Explore and visualize a few images from the dataset.

3. **Build a Convolutional Neural Network (CNN):**
   - Create a CNN model suitable for image classification.
   - Design the architecture with convolutional layers, pooling layers, and dense layers.
   - Compile the model with an appropriate optimizer, loss function, and metric.

4. **Train the Model:**
   - Train the model on the SVHN training data.
   - Monitor the training process using validation data.
   - Aim for high accuracy and consider experimenting with hyperparameters.

5. **Evaluate the Model:**
   - Evaluate the trained model on the SVHN test data.
   - Analyze the classification performance and accuracy.

6. **Visualize Predictions:**
   - Choose a few images from the test set and visualize the model's predictions.
   - Explore cases where the model succeeded and where it might have struggled.

