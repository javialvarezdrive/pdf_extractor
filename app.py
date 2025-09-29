
import streamlit as st
import PyPDF2
import io

st.title("Extractor de Texto de PDF")

uploaded_file = st.file_uploader("Sube un archivo PDF", type="pdf")

if uploaded_file is not None:
    st.write("Archivo subido exitosamente.")
    
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        st.text_area("Texto extraído", text, height=300)
        
        # Create a text file in memory
        text_file = io.StringIO(text)
        
        # Provide a download button
        st.download_button(
            label="Descargar texto como .txt",
            data=text_file.getvalue(),
            file_name="texto_extraido.txt",
            mime="text/plain"
        )
        
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
