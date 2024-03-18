import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTaUESVFbUnxC9q5-d-BiQXk6JD4r--bTZ3lNcryvfCeKqJq-tnz3VLhPwS_bZ5WXsRGYkOrtgkLlTU/pub?output=csv')
st.dataframe(voc)
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Definition'].value[i]
word_chi=voc['Hanzi'].values[i]
st.write(word_fr+"Hanzi"+word_chi)
