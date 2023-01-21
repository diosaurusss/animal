import streamlit as st

tab1, tab2, tab3 = st.tabs(["KARNIVORA", "OMNIVORA", "HERBIVORA"])

with tab1:
   st.header("KARNIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN KARNIVORA')

with tab1:
   st.header("OMNIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN KARNIVORA')

with tab1:
   st.header("HERBIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN KARNIVORA')