from itertools import chain
import streamlit as st
from base_model import stream_response_from_llm
st.set_page_config(page_title="CHAT MAMA", page_icon="👩‍💼", layout="centered")

st.title("CHAT MAMA")

# 세션 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 질문 입력
user_input = st.chat_input("무엇이든지 부탁하세요")

if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # GPT 응답 스트리밍
    with st.chat_message("assistant"):
        full_response = st.empty()
        accumulated = ""
        for chunk in stream_response_from_llm(user_input):  # ✅ 핵심
            accumulated += chunk
            full_response.markdown(accumulated + "▌")
        full_response.markdown(accumulated)

    st.session_state.messages.append({"role": "assistant", "content": accumulated})
