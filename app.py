import streamlit as st
from src.pdf_extractor import extract_text_from_pdf
from src.clause_extraction import extract_clauses
from src.classification import classify_clauses
from src.summarization import summarize_text
from src.similarity import calculate_similarity


st.set_page_config(
    page_title="Legal Document Analyzer",
    layout="wide"
)

st.title("Legal Document Analyzer")
st.write("Analyze legal documents using Natural Language Processing.")

uploaded_file = st.file_uploader(
    "Upload a Legal PDF",
    type=["pdf"]
)

if uploaded_file:

    file_path = "temp_document.pdf"

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    text = extract_text_from_pdf(file_path)

    if not text:
        st.error("No text could be extracted from the PDF.")
        st.stop()

    st.success("Document processed successfully.")

    clauses = extract_clauses(text)
    classified_clauses = classify_clauses(clauses)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Document",
        "Clauses",
        "Summary",
        "Similarity"
    ])

    with tab1:
        st.subheader("Extracted Text")

        st.text_area(
            "Document Content",
            text,
            height=500
        )

    with tab2:
        st.subheader("Legal Clauses")

        if classified_clauses:

            for clause in classified_clauses:

                st.markdown(
                    f"### Section {clause['section']}: {clause['title']}"
                )

                st.write(
                    f"**Category:** {clause['category']}"
                )

                st.write(clause["content"])

                st.divider()

        else:
            st.write("No clauses detected.")

    with tab3:
        st.subheader("Document Summary")

        summary = summarize_text(
            text,
            num_sentences=8
        )

        st.write(summary)

    with tab4:
        st.subheader("Document Similarity")

        second_file = st.file_uploader(
            "Upload another legal PDF",
            type=["pdf"],
            key="similarity_file"
        )

        if second_file:

            second_path = "temp_document_2.pdf"

            with open(second_path, "wb") as file:
                file.write(second_file.getbuffer())

            second_text = extract_text_from_pdf(
                second_path
            )

            similarity = calculate_similarity(
                text,
                second_text
            )

            st.metric(
                "Text Similarity",
                f"{similarity}%"
            )

            st.write(
                "Similarity is calculated using TF-IDF and cosine similarity."
            )