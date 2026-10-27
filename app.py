import streamlit as st
from PyPDF2 import PdfReader

st.title("나만의 맞춤형 PDF AI 비서 🤖")

# 1. 파일 업로드 UI 및 입력 기능
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")
user_question = st.chat_input("문서에 대해 무엇이든 물어보세요!")

# 2. 데이터 처리 및 AI 연동 기능
if uploaded_file is not None:
    try: 
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            
        if not text.strip():
            raise ValueError("텍스트 없음") 
            
        # 텍스트가 정상 추출되었을 때만 질문 받기
        if user_question:
            st.chat_message("user").write(user_question)
            
            # AI 답변 생성 로직 (가상)
            ai_response = f"분석된 결과: 입력하신 '{user_question}'에 대한 답변입니다." 
            
            # 3. 결과 출력 기능
            st.chat_message("assistant").write(ai_response)
            
    except Exception as e:
        # 에러 발생 시 프로그램 종료를 막고 경고창 띄우기
        st.error("텍스트를 추출할 수 없는 PDF 파일입니다. 정상적인 파일을 업로드해주세요.")
