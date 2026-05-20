import streamlit as st
import tempfile

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader

from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

# PAGE CONFIG
st.set_page_config(
    page_title="Local AI PDF Chatbot",
    page_icon="🤖",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput input {
    background-color: #1E1E1E;
    color: white;
    border-radius: 10px;
    border: 1px solid #333;
}

.stFileUploader {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
}

.chat-box {
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    background-color: #1A1A1A;
    border: 1px solid #333;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    color: #AAAAAA;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("⚡ Local RAG AI")
    st.markdown("---")
    st.markdown("""
    ### Features
    - 📄 PDF Chat
    - 🧠 Local LLM
    - 🔍 Semantic Search
    - 💻 Ollama Powered
    """)

    st.markdown("---")
    st.caption("Built with LangChain + Ollama")

# MAIN TITLE
st.markdown('<div class="big-title">🤖 AI PDF Assistant</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Upload a PDF and chat with your document locally.</div>',
    unsafe_allow_html=True
)

# FILE UPLOAD
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:

    with st.spinner("📚 Processing your PDF..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        texts = text_splitter.split_documents(documents)

        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        db = Chroma.from_documents(texts, embeddings)

    st.success("✅ PDF processed successfully!")

    query = st.text_input("Ask something about your PDF")

    if query:

        with st.spinner("🤖 Thinking..."):

            docs = db.similarity_search(query)

            llm = ChatOllama(model="llama3")

            context = "\n".join([doc.page_content for doc in docs])

            prompt = f"""
            Answer the question based on the context below.

            Context:
            {context}

            Question:
            {query}
            """

            response = llm.invoke(prompt)

            st.markdown(f"""
            <div class="chat-box">
                <h4>🤖 AI Response</h4>
                <p>{response.content}</p>
            </div>
            """, unsafe_allow_html=True)