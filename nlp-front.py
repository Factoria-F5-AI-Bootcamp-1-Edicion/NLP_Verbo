from enum import auto
import streamlit as st
import pandas as pd
import warnings
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import r2_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from streamlit_option_menu import option_menu
import pickle
#from streamlit_option_menu import option_menu
import time
import requests


import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

from xgboost import XGBClassifier


warnings.filterwarnings("ignore")
  
#Lottie Animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets7.lottiefiles.com/packages/lf20_3vbOcw.json"
lottie_url_download = "https://assets10.lottiefiles.com/packages/lf20_q56zavhf.json"
lottie_url_transition1= "https://assets10.lottiefiles.com/temp/lf20_tXDjQg.json"
lottie_url_home = "https://assets10.lottiefiles.com/packages/lf20_xgdvjjxc.json"
lottie_url_predict = "https://assets7.lottiefiles.com/packages/lf20_feesoomz.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_home = load_lottieurl(lottie_url_home)
lottie_download = load_lottieurl(lottie_url_download)
lottie_transition1 = load_lottieurl(lottie_url_transition1)
lottie_predict = load_lottieurl(lottie_url_predict)

#MENU 
# Funcion para reducir el margen top
def margin(): 
    st.markdown("""
            <style>
                .css-18e3th9 {
                        padding-top: 1rem;
                        padding-bottom: 10rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                .css-1d391kg {
                        padding-top: 3.5rem;
                        padding-right: 1rem;
                        padding-bottom: 3.5rem;
                        padding-left: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)



        
#MENU 
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            
            selected = option_menu(
                menu_title="Menu",  # required
                options=["Home", "Prediction",],  # required
                icons=["house","clipboard-plus",],  # optional
                #menu_icon= "cast",  # optional
                default_index=0,  # optional
                styles={
                    "menu-icon":"Data",
                    
                    "menu_title":{"font-family": "Tahoma"},
                    "nav-link": {"font-family": "Tahoma", "text-align": "left", "margin":"0px",},
                    #"nav-link-selected": {""}, 
                    })
        return selected



selected = streamlit_menu(example=EXAMPLE_NO)


if selected == "Home":

    st.markdown("<h1 style='text-align: center; color: purple;'>DeepIA Tech</h1>", unsafe_allow_html=True)
    

    st.image("Healthy.png")
    
    st.markdown("<h5 style='text-align: justify; color: black;'>DeepIA Tech es una consultoría en la que nos encargamos de buscar soluciones tecnológicas. Nuestro equipo está conformado por data analystics, desarrolladores y desarrolladoras de Inteligencia Artificial, especialistas en marketing y diseño web.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: black;'>Así nace Healthy Comments es una aplicación para el análisis de comentarios, como en las redes sociales, que nos ayuda a identificar si son tóxicos o no, utilizando Machine Learning. Queremos seguir desarrollando nuestra herramienta  para que sea mas polivalente e incluso llegar a poder restringir de manera automática los comentarios nocivos hacia otras personas.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: black;'>Contamos con soporte técnico que ayuda a mantener la herramienta de forma constante y ofrecemos capacitación a las empresas.</h5>", unsafe_allow_html=True)



if selected== "Prediction":
    margin()
    st.markdown("<h1 style='text-align: center; color: purple;'>Ingresa el comentario a clasificar en la cajita de abajo</h1>", unsafe_allow_html=True)

    st_lottie(lottie_predict, key="predict",
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        
        height=None,
        width=None,
        ) 



    txt = st.text_area('Aqui va tu comentario para clasificar', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')


    
    
 
    
    
    


    if st.button("Predict"):
        
            
        with st_lottie_spinner(lottie_download, key="download"):
            time.sleep(4)
            
            

            st.write("Stroke Probability", 
                str(round(predict[0][1],2)) , " %" )
            
            

    









