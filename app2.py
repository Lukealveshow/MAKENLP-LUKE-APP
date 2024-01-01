# app.py
import streamlit as st
from deep_translator import GoogleTranslator
from summarization import summarize_text
from generation import generate_answer
from database import get_mongo_client, insert_data_mongodb

# Obter o cliente MongoDB
mongo_client = get_mongo_client()

def translate_page(language):
    # Using deep_translator for page translation
    translator = GoogleTranslator(source='auto', target=language)
    translated_title = translator.translate("Seja Bem Vindo ao MAKENLP")
    st.title(translated_title)
    
    # Additional fields
    translated_name = translator.translate("Nome:")
    name = st.text_input(translated_name)
    
    translated_age = translator.translate("Idade:")
    age = st.number_input(translated_age, step=1)
    
    translated_gender = translator.translate("Gênero:")
    gender_options = [translator.translate('Masculino'), translator.translate('Feminino')]
    gender = st.selectbox(translated_gender, options=gender_options)
    
    # Section for text input
    translated_text_input = translator.translate("Digite o texto para resumir:")
    st.subheader(translated_text_input)
    text_summarization = st.text_area("", height=150)
    
    # Button to summarize text
    if st.button(translator.translate("Resumir Texto")):
        summarized_text = summarize_text(text_summarization)
        st.subheader(translator.translate("Texto Resumido"))
        st.write(summarized_text)
    
    translated_text_gen = translator.translate("Digite o texto:")
    st.subheader(translated_text_gen)
    text_generation = st.text_area("", height=150, key='text_generation')
    
    translated_question = translator.translate("Faça uma pergunta sobre o texto:")
    question = st.text_input(translated_question, key='question')

    # Restante do código...

    # Button to execute all functions and insert into the database
    if st.button(translator.translate("Enviar")):
        summarized_text = summarize_text(text_summarization)
        answer = generate_answer(question, text_generation)
        translated_text = GoogleTranslator(source='auto', target=language).translate(text_translation)

        # Utilize a função insert_data_mongodb do database.py
        insert_data_mongodb(name, age, gender, text_summarization, summarized_text, text_generation,
                            question, answer, text_translation, language, translated_text)
        st.success(translator.translate("Dados inseridos com sucesso!"))

# Run the Streamlit app
if __name__ == '__main__':
    st.set_page_config(page_title="MAKENLP", page_icon=":speech_balloon:")
    translation_language = st.selectbox("Selecione o idioma de tradução:", options=['pt', 'en', 'fr', 'es'])
    translate_page(translation_language)