import streamlit as st
import hashlib

document_hashes = {}

def generate_document_hash(document_content):
    hash_object = hashlib.sha256(document_content.encode())
    return hash_object.hexdigest()

def notarize_document(document_content):
    document_hash = generate_document_hash(document_content)
    document_hashes[document_hash] = document_content
    return document_hash

def verify_document(document_hash):
    return document_hash in document_hashes

# Streamlit UI

st.set_page_config(
    page_title="Digital Notary System",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Digital Notary System")

# Page 1: Document Uploading
if 'document_hash' not in st.session_state:
    st.header("Upload Document for Notarization")
    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf'])

    if uploaded_file:
        document_content = uploaded_file.read()
        document_hash = notarize_document(document_content.decode())
        st.session_state.document_hash = document_hash
        st.success("Document Notarized Successfully!")
        st.write("Document Hash:", document_hash)
else:
    st.header("Document Notarized")
    st.write("Document Hash:", st.session_state.document_hash)

# Page 2: Digital Checking
st.header("Digital Document Checking")
verification_hash = st.text_input("Enter Document Hash to Verify")

if verification_hash:
    is_authentic = verify_document(verification_hash)
    if is_authentic:
        st.success("Document is Authentic!")
    else:
        st.error("Document is Not Authentic!")
