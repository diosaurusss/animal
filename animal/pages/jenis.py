import streamlit as st

tab1, tab2, tab3 = st.tabs(["KARNIVORA", "HERBIVORA", "OMNIVORA"])

with tab1:
   st.header("KARNIVORA")
   st.subheader('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN KARNIVORA : ')
   st.markdown('1.   SINGA')
   st.image("animal/pages/singa.jpg")
   st.markdown('berikut ini adalah suara singa')
   st.audio("animal/pages/suara singa.mp3")
   
   st.markdown('1.   HARIMAU')
   st.image("animal/pages/harimau.jpg")
   st.markdown('berikut ini adalah suara harimau')
   st.audio("animal/pages/suara singa.mp3")

with tab2:
   st.header("HERBIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN HERBIVORA : ')

with tab3:
   st.header("OMNIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN OMNIVORA  : ')
