import streamlit as st

tab1, tab2, tab3 = st.tabs(["KARNIVORA", "HERBIVORA", "OMNIVORA"])

with tab1:
   st.header("KARNIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN KARNIVORA : ')

with tab2:
   st.header("HERBIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN HERBIVORA : ')

with tab3:
   st.header("OMNIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN OMNIVORA  : ')
