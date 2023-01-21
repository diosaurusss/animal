
import streamlit as st

st.set_page_config(
    page_title="ANIMALCLUB")

st.title("SELAMAT DATANG DI ANIMAL CLUB")
st.sidebar.success("Pilih Halaman")

st.subheader("Hai Sobat")
    
st.write(
        "Selamat Datang Di WEB Pengenalan Hewan"
    )

st.write("---")

st.header("Apa Itu Hewan?")
st.write("##")
st.write(
            """
            Pengertian Hewan
            Menurut Anshori (2009) hewan atau disebut juga dengan binatang adalah 
            kelompok organisme yang diklasifikasikan dalam kerajaan Animalia atau 
            metazoa, adalah salah satu dari berbagai makhluk hidup di bumi. Sebutan lainnya 
            adalah fauna dan margasatwa (atau satwa saja). Hewan dalam pengertian 
            sistematika modern mencakup hanya kelompok bersel banyak (multiselular) dan 
            terorganisasi dalam fungsi-fungsi yang berbeda (jaringan), sehingga kelompok ini 
            disebut juga histozoa. Semua binatang heterotrof, artinya tidak membuat energi 
            sendiri, tetapi harus mengambil dari lingkungan sekitarnya.
            """
        )
st.header("Playlist Fundamental Streamlit")
col1, col2, col3 = st.columns(3)

with col1:
        st.subheader("Introduction di Aplikasi Streamlit")
        st.video('https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l')

with col2:
        st.subheader("Cara menampilkan teks")
        st.video('https://www.youtube.com/watch?v=tPA0x_wToXQ&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=2')

with col3:
        st.subheader("Cara Menampilkan Data")
        st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')
    
st.write("---")
