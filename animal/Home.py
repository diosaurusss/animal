
import streamlit as st

st.set_page_config(
    page_title="ANIMALCLUB")

st.title("SELAMAT DATANG DI ANIMAL CLUB")
st.sidebar.success("Pilih Halaman")

st.subheader("Hai Sobat")
    
st.write(
        "Selamat Datang Di WEB Pengenalan Hewan Vertebrata"
    )

st.write("---")

st.header("Apa Itu Hewan Vertebrata?")
st.write("##")
st.write("Pengertian Hewan Vertebrata")
st.write(
            """
            Hewan vertebrata adalah golongan hewan yang memiliki tulang belakang.
            Tulang belakang berasal dari perkembangan sumbu penyokong tubuh primer atau notokorda (korda dorsalis).
            Notokorda vertebrata hanya ada pada masa embrionik,
            setelah dewasa akan mengalami penulangan menjadi sistem penyokong tubuh sekunder, 
            yaitu tulang belakang (vertebrae).

            Dalam sistem klasifikasi, vertebrata merupakan subfilum dari filum Chordata. 
            Chordata meliputi hewan-hewan yang memiliki ciri-ciri sebagai berikut :

            1.  Memiliki notokord, yaitu kerangka berbentuk batangan keras tetapi lentur.
                Notokord terletak di antara saluran pencernaan dan tali saraf, memanjang sepanjang tubuh membentuk sumbu kerangka.
            2.  Memiliki tali saraf tunggal, berlubang terletak dorsal terhadap notokord, dan memiliki ujung anterior  yang membesar berupa otak.
            3.  Memiliki ekor yang memanjang ke arah posterior terhadap anus.
            4.  Memiliki celah faring.
            """
        )

st.write("---")

st.header("Ciri - Ciri Hewan Vertebrata")
st.write("##")
st.write(
            """
            Tubuh hewan vertebrata mempunyai tipe simetri bilateral dan bagian organ dalam 
            dilindungi oleh rangka dalam atau endoskeleton, khusus bagian otak yang dilindungi oleh tulang-tulang tengkorak (kranium).
            Bagian terluar tubuh hewan vertebrata berupa kulit yang tersusun atas epidermis (lapisan luar) dan dermis (lapisan dalam).
            
            Kulit hewan vertebrata ada yang tertutup dengan bulu dan ada juga yang tertutup dengan rambut.
            Organ dalam, seperti organ pencernaan, jantung, dan pernapasan terdapat didalam suatu rongga tubuh atau selom.
            Selain itu, hewan vertebrata memiliki alat tubuh yang lengkap, yang menyusun sistem organ tubuhnya meliputi sistem pencernaan yang memanjang dari mulut hingga anus,
            sistem peredaran darah tertutup (darah mengalir di dalam pembuluh darah), alat ekskresi berupa ginjal, alat pernapasan berupa paru-paru atau insang, 
            sepasang alat reproduksi (kanan dan kiri) serta sistem endokrin yang berfungsi menghasilkan hormon. Berikut ciri-ciri lainnya dari hewan vertebrata:
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
