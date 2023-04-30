import pickle
import numpy as np
import streamlit as st

#Load save model
model = pickle.load(open('Model_Heart_Desease.sav','rb'))

#Judul web
st.title('Prediksi Penyakit Jantung')
st.subheader(':blue[_by Krishnadana_]:sunglasses:')

#Form input data (Harus sama dengInsulinan nama coloumn pada data)

# Membuat Input menjadi 2 Colomn
col1, col2,col3 = st.columns(3)

with col1:
    age = st.number_input('Umur',0)

with col1:
    sex = st.number_input('Jenis Kelamin',0)

with col1:
    cp = st.number_input('Jenis Nyeri Dada',0)

with col1:
    trestbps = st.number_input('Tekanan Darah',0)

with col1:
    chol = st.number_input('Nilai Kolestrol',0)

with col2:
    fbs = st.number_input('Gula Darah',0)

with col2:
    restecg = st.number_input('Hasil Elektrokadiografi',0)

with col2:
    thalach = st.number_input('Detak jantung Maksimum',0)

with col2:
    exang = st.number_input('Induksi Angina',0)

with col3:
    oldpeak =  st.number_input('ST Depression')

with col3:
    slope =  st.number_input('Slope',0)

with col3:
    ca =  st.number_input('Nilai CA',0)

with col3:
    thal =  st.number_input('Nilai Thal',0)


# code untuk diagnosis
heart_diagnosis = ''

# membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if (heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'


st.success(heart_diagnosis)

