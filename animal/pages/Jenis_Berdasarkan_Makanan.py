import streamlit as st

st.title("INI ADALAH JENIS HEWAN BERDASARKAN MAKANAN")

tab1, tab2, tab3 = st.tabs(["KARNIVORA", "HERBIVORA", "OMNIVORA"])

with tab1:
   st.header("KARNIVORAA")
   st.subheader('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN KARNIVORA : ')
   st.markdown('1.   SINGA')
   st.image("animal/pages/singa.jpg")
   st.markdown('berikut ini adalah suara singa')
   st.audio("animal/pages/suara singa.ogg")
   
   st.markdown('2.   HARIMAU')
   st.image("animal/pages/harimau.jpg")
   st.markdown('berikut ini adalah suara harimau')
   st.audio("animal/pages/suara harimau.mp3")

with tab2:
   st.header("HERBIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN HERBIVORA : ')

with tab3:
   st.header("OMNIVORA")
   st.caption('BERIKUT INI ADALAH BEBERAPA CONTOH HEWAN OMNIVORA  : ')
