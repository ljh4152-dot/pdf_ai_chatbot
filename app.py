import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

st.title("나만의 맞춤형 PDF AI 비서 🤖")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 내 API 키로 사용 가능한 모델을 자동으로 찾아 연결
model_name = "gemini-1.5-flash"
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        model_name = m.name
        break

model = genai.GenerativeModel(model_name)

uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")
user_question = st.chat_input("문서에 대해 무엇이든 물어보세요!")

if uploaded_file is not None:
    try:
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            
        if not text.strip():
            raise ValueError("텍스트 없음")
            
        if user_question:
            st.chat_message("user").write(user_question)
            
            prompt = f"다음 문서 내용을 바탕으로 질문에 답해줘.\n\n문서 내용: {text}\n\n질문: {user_question}"
            response = model.generate_content(prompt)
            
            st.chat_message("assistant").write(response.text)
            
    except Exception as e:
        st.error(f"에러 원인: {e}")
