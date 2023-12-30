import streamlit as st
import pandas as pd

# Função para inserir dados no banco de dados
def insert_data(name, age, gender, text_summarization, summarized_text, text_generation,
                question, answer, text_translation, language, translated_text):
    try:
        # Inicializa a conexão com o banco de dados
        conn = st.connection('mysql', type='sql')
        
        # Cria um DataFrame com os dados
        data = {
            'name': [name],
            'age': [age],
            'gender': [gender],
            'text_summarization': [text_summarization],
            'summarized_text': [summarized_text],
            'text_generation': [text_generation],
            'question': [question],
            'answer': [answer],
            'text_translation': [text_translation],
            'language': [language],
            'translated_text': [translated_text]
        }

        df = pd.DataFrame(data)

        # Executa a inserção no banco de dados
        conn.insert('mytable', df)

        st.success("Dados inseridos com sucesso!")
    
    except Exception as e:
        st.error(f"Erro ao inserir dados: {e}")

