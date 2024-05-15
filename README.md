# Turkish Diacritization Project

## Description
This repository contains the implementation of a deep learning model for correcting diacritization errors in Turkish text. The model uses a sequence-to-sequence architecture with a bidirectional LSTM encoder and LSTM decoder to accurately predict diacritic marks. The goal is to enhance the readability and semantic accuracy of Turkish text in digital communications.

## Installation

### Prerequisites
- Python 3.8 or higher
- PyTorch 1.8 or newer
- pandas

### Setup
To set up the project environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mburaozkan/YZV405_2324_150200337_150210903.git

2. Navigate to the project directory:
   ```bash
   cd  YZV405_2324_150200337_150210903

3. Install the required packages:
   ```bash
    pip install torch torchvision pandas

## Usage

This project includes two Jupyter notebooks: 'NLP_FINAL.ipynb' for training the model and 'NLP_Test.ipynb' for testing and evaluation.

## Training the Model

To train the model, open the NLP_FINAL.ipynb notebook and follow the instructions therein. Make sure to adjust hyperparameters as necessary based on your dataset.
Testing the Model

Once the model is trained, you can evaluate its performance using the NLP_Test.ipynb notebook. This notebook provides utilities to test the model against a test dataset and visualize the results.
