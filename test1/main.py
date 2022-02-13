import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
st.title('streamlit 超入門')
# st.write("DataFrame")
st.write("Image")

st.write('Display Image')

img = Image.open('main_1.jpg')
st.image(img, caption='king', use_column_width=True)

# df = pd.DataFrame(
#   np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#   columns=['lat', 'lon']
# )

# # st.table(df.style.highlight_max(axis=0))
# # st.line_chart(df)
# st.map(df)


