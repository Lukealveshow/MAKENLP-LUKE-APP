import os
from pymongo import MongoClient
import streamlit as st

# Obter a URI do MongoDB a partir das variáveis de ambiente
MONGO_URI = os.getenv("mongodb+srv://Lucasluke:Lucas1710@dados.brvclaf.mongodb.net/?retryWrites=true&w=majority")

# Verificar se a URI foi definida
if MONGO_URI is None:
    st.error("A URI do MongoDB não foi configurada. Verifique suas variáveis de ambiente.")
else:
    try:
        # Tentar criar a conexão com o MongoDB
        client = MongoClient(MONGO_URI)

        # Acessar o banco de dados e a coleção
        db = client.app_dados
        data_collection = db.data

        # Interface do Streamlit para inserir dados
        st.header("Inserir Dados no MongoDB")
        name = st.text_input("Nome:")
        age = st.number_input("Idade:", step=1)
        gender = st.selectbox("Gênero:", ["Masculino", "Feminino"])

        # Botão para inserir dados
        if st.button("Inserir Dados"):
            # Dados a serem inseridos
            data = {
                'name': name,
                'age': age,
                'gender': gender
            }

            # Inserir dados no MongoDB
            data_collection.insert_one(data)

            st.success("Dados inseridos com sucesso!")

    except Exception as e:
        # Lidar com erros de conexão
        st.error(f"Erro ao conectar ao MongoDB: {e}")
