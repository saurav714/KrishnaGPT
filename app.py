import os
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub
import pyttsx3

# Step 1: Load Mahabharata text
def load_maha_texts(folder='maha_texts'):
    texts = []
    if not os.path.exists(folder):
        st.error("Mahabharata text folder not found!")
        return ""
    for file in sorted(os.listdir(folder)):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                texts.append(f.read())
    return "\n".join(texts)


# Step 2: Split and Embed
def create_vector_db(text):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_texts(chunks, embeddings)
    return db

# Step 3: Load QA Chain
def create_chain():
    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.5, "max_length": 256})
    return load_qa_chain(llm, chain_type="stuff")

# Step 4: Krishna Voice (TTS)
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 135)
    engine.setProperty("voice", engine.getProperty("voices")[1].id)  # Adjust for Krishna-style calm male voice
    engine.say(text)
    engine.runAndWait()

# Streamlit App
st.title("🕉️ Krishna GPT - Wisdom from Mahabharata")

query = st.text_input("Ask Krishna:", "")

if query:
    st.info("Thinking like Krishna...")

    # Load data only once
    if "db" not in st.session_state:
        maha_text = load_maha_texts()
        st.session_state.db = create_vector_db(maha_text)
        st.session_state.chain = create_chain()

    docs = st.session_state.db.similarity_search(query)
    result = st.session_state.chain.run(input_documents=docs, question=query)

    st.success(result)
    speak(result)
