from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Калькулятор риска гестационного уросепсиса",
    page_icon="🩺",
    layout="centered",
)

# Убираем стандартные отступы и меню Streamlit, чтобы был виден только калькулятор
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Тот же визуал, что и в HTML-версии: карточки, кнопки Да/Нет, расчёт по формуле
html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1150, scrolling=True)
