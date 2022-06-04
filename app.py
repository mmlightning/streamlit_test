from datetime import date, datetime
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.write("# Finanzentwicklung Matthias Machinek 💸!")

rate = st.slider(
     'Wähle Deinen Stundenlohn',
     0,1000,200,1)
st.write('Stundenlohn [Euro]:', rate)

x = np.arange(0,720,1)
y = rate*x/1E6

fig,ax=plt.subplots(1,1,figsize=(10,6))

ax.plot(x,y)
ax.set_ylim(0,1)
ax.set_xlim(0,720)
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.set_xlabel("Monatliche Arbeitsstunden")
ax.set_ylabel("Monatliches Bruttoeinkommen [Million Euro]")
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
for item in [fig, ax]:
    item.patch.set_visible(False)
st.pyplot(fig)
