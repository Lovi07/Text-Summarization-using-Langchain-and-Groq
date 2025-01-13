import os
import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
import tempfile

# Streamlit App Configuration
st.set_page_config(page_title="LangChain: Summarize Text From YT, Website, or PDF", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT, Website, or PDF")
st.subheader("Summarize Content from a URL or Uploaded PDF")

# Sidebar: API Key Inputs
with st.sidebar:
    st.write("get your groq api key from https://groq.com/ and get your langsmith api key from https://langsmith.com/")
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
    langsmith_api_key = st.text_input("LangSmith API Key", value="", type="password")  # LangSmith API Key

# Set LangSmith environment variables
if langsmith_api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key

# URL Input
generic_url = st.text_input("URL (YouTube or Website)", label_visibility="collapsed")

# PDF File Uploader
uploaded_file = st.file_uploader("Upload a PDF File", type=["pdf"])

# Prompt Template for Summarization
initial_prompt_template = """
Write a concise summary of the following content:
Content: {text}
"""
initial_prompt = PromptTemplate(template=initial_prompt_template, input_variables=["text"])

# Define the refinement prompt
refinement_prompt_template = """
The following is a summary that needs refinement:
Current Summary: {existing_answer}

We have additional content that can be used to refine the summary:
Content: {text}

Please refine the current summary to include the new information while maintaining conciseness.
"""
refinement_prompt = PromptTemplate(template=refinement_prompt_template, input_variables=["existing_answer", "text"])

# Initialize LLM with Groq API Key
if groq_api_key:
    try:
        llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)
    except Exception as e:
        st.error(f"Failed to initialize Groq client: {e}")

# Button to Summarize Content
if st.button("Summarize the Content"):
    if not groq_api_key.strip():
        st.error("Please provide the Groq API Key to get started.")
    elif not langsmith_api_key.strip():
        st.error("Please provide the LangSmith API Key for tracking.")
    elif not (generic_url.strip() or uploaded_file):
        st.error("Please provide a valid URL or upload a PDF file.")
    elif generic_url and not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video or website URL.")
    else:
        try:
            with st.spinner("Processing..."):
                # Load content from URL (YouTube or Website)
                if generic_url.strip():
                    if "youtube.com" in generic_url:
                        loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                    else:
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=False,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                            },
                        )
                    docs = loader.load()

                # Load content from uploaded PDF
                elif uploaded_file:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                        temp_file.write(uploaded_file.read())
                        temp_file_path = temp_file.name
                    
                    # Load the PDF using PyPDFLoader
                    loader = PyPDFLoader(temp_file_path)
                    docs = loader.load_and_split()

                # Summarize the content with LangSmith tracking enabled
                chain = load_summarize_chain(
                    llm,
                    chain_type="refine",
                    question_prompt=initial_prompt,
                    refine_prompt=refinement_prompt,
                    verbose=True
                )
                output_summary = chain.run(docs)

                # Display the summary
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")
