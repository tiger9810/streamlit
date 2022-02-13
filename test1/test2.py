import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
st.title('streamlit 超入門')
# st.write("DataFrame")
st.write("Image")

st.write('Display Image')

if st.checkbox('Show image'):
  img = Image.open('main_1.jpg')
  st.image(img, caption='king', use_column_width=True)
