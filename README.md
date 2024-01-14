# QnA Chatbot Using PDF

## Overview
This project is focused on developing a Question and Answer (QnA) Chatbot that utilizes PDF documents to answer queries. It provides an interactive interface for users to ask questions and receive relevant answers extracted from PDF content.

## Features
- **Chatbot GUI**: An interactive Graphical User Interface.
- **PDF Question Answering**: Process and answer questions based on PDF content.
- **Model Training Notebooks**: Jupyter notebooks for training sentence transformer models.
- **Trained Models**: Pre-trained models using sentence transformers.

## Contents
- `CHATBOT.pptx`: PowerPoint presentation detailing the chatbot project.
- `Chatbot_GUI`: Files for the Chatbot's graphical user interface.
- `Model_trained`: Trained weights of the transformer models.
- `pytorch_sbert_training.ipynb`: Jupyter notebook for training a model using PyTorch and SBERT.
- `requirements.txt`: Lists necessary Python packages.
- `sbert_test_c`: Additional resources or tests related to SBERT.
- `sentence_transformer_training.ipynb`: Notebook for training sentence transformer models.
- `testing.ipynb`: Notebook for testing and evaluating the models.

## Installation
1. Clone this repository.
2. Install required packages using `pip install -r requirements.txt`.

## Usage
### Chatbot GUI:
- Navigate to the `Chatbot_GUI` directory.
- Start the application following the provided instructions.
- The Chatbot GUI is ready for use upon launch.

### Sentence Model and GPT API Key:
- Pre-trained sentence model hosted on Hugging Face is integrated within the Chatbot via LangChain.
- Responses are formulated after comparing embeddings with the database content.
- GPT API is used with a secret key (free trial version). Update the key in `utils.py` at the start of the Chatbot_GUI folder.

## Working with PDFs:
- Chatbot allows PDF uploads.
- Ask questions based on the PDF's content.
- Chatbot processes queries and returns answers extracted from the uploaded PDF.

## Model Training and Weights
### Model Weights
- `Model_trained` Folder: Contains weights for a transformer model, trained for understanding user queries.
- `sbert_train` Folder: Stores weights for another model, possibly fine-tuned for processing responses from PDFs.

### Training Notebooks
- `pytorch_sbert_training.ipynb`: Details the training process of the model in `Model_trained`, using PyTorch and SBERT.
- `sentence_transformer_training.ipynb`: Corresponds to the model in `sbert_train`, outlining the training approach and parameters used.

## Integrating Models with Chatbot
- Models are crucial for the chatbot's functionality, with one handling user queries and the other processing PDF content to generate responses.

## Using Only Chatbot Feature
### Chatbot GUI:
- To use the Chatbot feature without model training, navigate to the `Chatbot_GUI` directory.
- Start the application following the provided instructions.
- The Chatbot GUI is ready for immediate use upon launch.

### Sentence Model and GPT API Key:
- Pre-trained sentence model integrated within the Chatbot via LangChain.
- Responses are formulated after comparing embeddings with the database content, then sent through the GPT API using a secret key.
- Note: The provided GPT API key is a free trial version and may need updating. Locate the key at the start of `utils.py` in the Chatbot_GUI folder to replace it with a new trial or paid version.

## Contributions
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
