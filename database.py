import streamlit as st
from pymongo import MongoClient
import ssl

# Criação do contexto SSL personalizado
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE
def insert_data_mongodb(name, age, gender, text_summarization, summarized_text, text_generation,
                        question, answer, text_translation, language, translated_text):
    try:
        client = MongoClient("mongodb+srv://Lucas:Lucas1717@cluster0.jm1yedl.mongodb.net/?retryWrites=true&w=majority",
                             tlsInsecure=True)

        db = client.data  # Nome do banco de dados
        data_collection = db.app_dados  # Nome da coleção

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

        data_collection.insert_one(data)

        st.success("Dados inseridos com sucesso!")

    except Exception as e:
        st.error(f"Erro ao inserir dados: {e}")
