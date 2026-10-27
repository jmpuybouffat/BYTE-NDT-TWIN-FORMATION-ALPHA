from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="BYTE NDT — TWIN FORMATION ALPHA",layout="wide")
st.title("BYTE NDT — TWIN FORMATION · ALPHA REV0 8512")
components.html(Path(__file__).with_name("operator_view.html").read_text(encoding="utf-8"),height=2100,scrolling=True)
