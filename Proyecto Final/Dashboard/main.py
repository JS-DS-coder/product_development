import streamlit as st
import numpy as np
import pandas as pd
from funciones import *


st.set_page_config(page_title='Covid-19',
                   page_icon='😷',
                   layout="wide")


#Sidebar
st.sidebar.header('COVID-19')

menu = st.sidebar.radio(
    "",
    ("Inicio", "Distribución geográfica", "Estadísticas de incrementos", "Otras estadísticas"),
)

st.sidebar.markdown('---')
st.sidebar.write("""
    Desarrollado por: 
    * Alejandro López 
    * Eddson Sierra 
    * Diego Alvarez 
    * Jairo Salazar 
    * Sergio Palma""")

st.sidebar.markdown('---')
st.sidebar.write("""
    Proyecto final\n 
    Product Development\n
    Universidad Galileo (2021)
""")
st.sidebar.image('images/galileo.png', width=75)

if menu == 'Inicio':
    set_inicio()
elif menu == 'Distribución geográfica':
    set_mapa()
elif menu == 'Estadísticas de incrementos':
    set_estadisticas()
elif menu == "Otras estadísticas":
    set_otras_estadisticas()