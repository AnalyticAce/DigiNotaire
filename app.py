import streamlit as st
import hashlib

document_hashes = []

def generate_document_hash(document_content):
    hash_object = hashlib.sha256(document_content.encode())
    return hash_object.hexdigest()

def notarize_document(document_content):
    document_hash = generate_document_hash(document_content)
    document_hashes.append((document_hash, document_content))
    return document_hash

def verify_document(document_hash):
    return document_hash in [hash_tuple[0] for hash_tuple in document_hashes]

st.set_page_config(
    page_title="Digital Notary System",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Digital Notary System")

st.header("Document Notarization")
uploaded_file = st.file_uploader("Upload Document for Notarization", type=['txt', 'pdf'])
if uploaded_file:
    document_content = uploaded_file.read()
    document_hash = notarize_document(document_content.decode('latin-1'))
    st.success("Document Notarized Successfully!")
    st.write("Document Hash:", document_hash)

st.header("Digital Document Verification")
verification_hash = st.text_input("Enter Document Hash to Verify")

if verification_hash:
    is_authentic = verify_document(verification_hash.strip())
    if is_authentic:
        st.success("Document is Authentic!")
        
        # Download the document with hash as filename
        download_link = f'<a href="data:application/octet-stream;base64,{document_content.decode("latin-1").encode("latin-1").hex()}" download="{verification_hash}.pdf">Download Document</a>'
        st.markdown(download_link, unsafe_allow_html=True)
        
    else:
        st.error("Document is Not Authentic!")
