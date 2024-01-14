# QnA Chatbot Using PDF

## Overview
This project is focused on developing a Question and Answer (QnA) Chatbot that utilizes PDF documents to answer queries. It's designed to provide an interactive interface for users to ask questions and receive relevant answers extracted from PDF content.

## Features
- **Chatbot GUI**: An interactive Graphical User Interface for easy interaction with the chatbot.
- **PDF Question Answering**: The ability to process and answer questions based on content available in PDF documents.
- **Model Training Notebooks**: Jupyter notebooks for training sentence transformer models on specific datasets.
- **Trained Models**: Includes pre-trained models using sentence transformers for immediate deployment.

## Contents
- `CHATBOT.pptx`: A PowerPoint presentation detailing the chatbot project.
- `Chatbot_GUI`: Directory containing files for the Chatbot's graphical user interface.
- `Model_trained`: Contains the trained weights of the transformer models.
- `pytorch_sbert_training.ipynb`: A Jupyter notebook for training a model using PyTorch and Sentence-BERT (SBERT).
- `requirements.txt`: Lists all the necessary Python packages required for the project.
- `sbert_test_c`: Additional model trained earlier weights files.
- `sentence_transformer_training.ipynb`: Notebook for training sentence transformer models.
- `testing.ipynb`: A notebook for testing and evaluating both sbert and sentence transformer models.

## Installation
To set up the project environment:
1. Clone this repository.
2. Install required packages using `pip install -r requirements.txt`.

## Usage
### Chatbot GUI:
- To use the Chatbot feature, navigate to the `Chatbot_GUI` directory.
- Start the application as per the instructions provided within the directory.
- The Chatbot GUI is ready for use upon launch.

### Sentence Model and GPT API Key:
- The weights for the customized sentence model are uploaded on Hugging Face and used in our LangChain implementation.
- After comparing embeddings from the database, the response is sent to the GPT API using a secret key (free trial version).
- Update the GPT API key in `utils.py` at the start of the Chatbot_GUI folder.

### Working with PDFs:
- Once the Chatbot is running, you can upload any PDF file.
- After uploading, you can ask questions from the content of the PDF, and the Chatbot will respond accordingly.

## Model Training and Weights
### Model Weights
- `Model_trained` Folder: Contains the weights for a transformer model, possibly trained for understanding user queries.
- `sbert_train` Folder: Stores weights for another model, possibly fine-tuned for fetching and processing responses from PDFs.

### Training Notebooks
- `pytorch_sbert_training.ipynb`: This notebook details the training process of the model in `Model_trained`, using PyTorch and SBERT.
- `sentence_transformer_training.ipynb`: Corresponds to the model in `sbert_train`, outlining the training approach and parameters used.

## Integrating Models with Chatbot
- The models are crucial for the chatbot's functionality, with one model handling user queries and the other processing PDF content to generate responses.

### Using Only Chatbot Feature
#### Chatbot GUI:
- To use the Chatbot feature without involving the model training aspects, simply navigate to the `Chatbot_GUI` directory.
- Start the application following the instructions provided within this directory.
- The Chatbot GUI is ready for immediate use upon launch, facilitating interaction through a user-friendly interface.

#### Sentence Model and GPT API Key:
- The pre-trained sentence model, hosted on Hugging Face, is integrated within the Chatbot via our LangChain implementation.
- Responses are formulated after comparing embeddings with the database content, then sent through the GPT API using a secret key.

## Contributions
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
