import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Função para inserir dados no banco de dados
def insert_data_mongodb(name, age, gender, text_summarization, summarized_text, text_generation,
                question, answer, text_translation, language, translated_text):
    try:
        # Obtenha a URL de conexão do arquivo secrets.toml
        mongo_url = st.secrets["mongo"]["mongodb+srv://Lucas:Lucas1717@cluster0.jm1yedl.mongodb.net/?retryWrites=true&w=majority"]

        # Conecte-se ao banco de dados MongoDB usando pymongo
        client = MongoClient(mongo_url)
        db = client.app_dados
        data_collection = db.data

        # Cria um documento com os dados
        data = {
            'name': name,
            'age': age,
            'gender': gender,
            'text_summarization': text_summarization,
            'summarized_text': summarized_text,
            'text_generation': text_generation,
            'question': question,
            'answer': answer,
            'text_translation': text_translation,
            'language': language,
            'translated_text': translated_text
        }

        # Insira o documento na coleção
        data_collection.insert_one(data)

        st.success("Dados inseridos com sucesso!")

    except Exception as e:
        st.error(f"Erro ao inserir dados: {e}")
