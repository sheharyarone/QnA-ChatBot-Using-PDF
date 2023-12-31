from langchain.document_loaders import PDFMinerLoader
import torch
import re
from langchain.docstore.document import Document
from sentence_transformers import SentenceTransformer
import os
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import time
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
pinecone.init(api_key="55657a9f-f09c-4762-9e4d-d416701bcd1e", environment="us-west4-gcp-free")


    

class ChatbotResponse:
    def __init__(self,path):
        self.embeddings = HuggingFaceEmbeddings(model_name='Shayaan69/test-model',model_kwargs={"device": "cuda"})
        self.path= path
        self.llm = OpenAI(temperature=0.0,api_key=os.environ['OPENAI_API_KEY'])
        self.chain =self.question_answerchain()
        self.doc_db = self.embed_docs()
        self.query = ""
        
        self.template = """Begin! Remember to use the user information to answer the questions.You should give your final answer in a concise manner.
Human: {question}
AI:
"""
        

    def load_pdf(self,path):
        text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size = 1200,
        chunk_overlap  = 200,
        length_function = len,
        is_separator_regex = False,
    )
        loader = PDFMinerLoader(path)
        data = loader.load()
        docs = text_splitter.create_documents([x.page_content for x in data])
        return docs
    


    def embed_docs(self):
        chunks = self.load_pdf(self.path)
        return FAISS.from_documents(chunks, self.embeddings)

            


#MAKING QA TOOLS 
    def question_answerchain(self):
       
        qatemplate = """You are a tax professional and a counsellor.Your job is to provide and guide users related to tax information
Given the following extracted parts of a long document and a question.
Try to ask further questions from the user if required or give an answer where requirement is fulfilled. 


%TONE:
- Your tone should be lawyered.
- Inquisitive


%CONTEXT:
{context}



Begin! Remember to use the context to answer the questions.Try to deduce the logic from the context where required and give to the point answer.You will only answer from the context. If you cant find the answer there say I donot know

Human: {question}
AI:"""
        qaprompt = PromptTemplate(
            input_variables=[ "question", "context"], template=qatemplate
        )
        chain1 = load_qa_chain(llm = self.llm, chain_type="stuff",verbose=False,prompt=qaprompt)
        return chain1
    
    def get_query_response(self,query):  
        docs=self.doc_db.similarity_search(query, k=4)
        response=self.chain.run({"question":query,"input_documents":docs})
        return response,docs


# if __name__ == '__main__':
#     print("Starting")
#     bot = ChatbotResponse(path = "../TaxDocument.pdf")
#     while True:
#         query = input("Enter your query: \n")
#         if query == "exit":
#             break
#         else:
#             print(bot.get_query_response(query))