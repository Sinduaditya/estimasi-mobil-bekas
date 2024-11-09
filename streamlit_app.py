import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav','rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga') :
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi harga Mobil Bekas dalam Ponds : ', predict)
    st.write('Estimasi harga Mobil Bekas dalam IDR (Juta) : ' , predict*20000)
    