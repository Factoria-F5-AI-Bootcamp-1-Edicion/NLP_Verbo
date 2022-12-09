#Importación librerias
import streamlit as st
import warnings
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie


warnings.filterwarnings("ignore")
  
#Lottie Animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_predict = "https://assets7.lottiefiles.com/packages/lf20_feesoomz.json"

lottie_predict = load_lottieurl(lottie_url_predict)

# FastAPI endpoint
url = 'http://fastapi:8008/predict/?'

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
                menu_title="Menú",  # required
                options=["Página principal", "Aplicación",],  # required
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


if selected == "Página principal":
    


    st.markdown("<h1 style='text-align: center; color: purple;'>DeepIA Tech</h1>", unsafe_allow_html=True)
   
    container = st.container()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image("Healthy.png")

    with col3:
        st.write(' ')
    #container.image("Healthy.png")
    
    st.markdown("<h5 style='text-align: justify; color: black;'>DeepIA Tech es una consultoría en la que nos encargamos de buscar soluciones tecnológicas. Nuestro equipo está conformado por data analystics, desarrolladores y desarrolladoras de Inteligencia Artificial, especialistas en marketing y diseño web.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: black;'>Así nace Healthy Comments es una aplicación para el análisis de comentarios, como en las redes sociales, que nos ayuda a identificar si son tóxicos o no, utilizando Machine Learning. Queremos seguir desarrollando nuestra herramienta  para que sea mas polivalente e incluso llegar a poder restringir de manera automática los comentarios nocivos hacia otras personas.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify; color: black;'>Contamos con soporte técnico que ayuda a mantener la herramienta de forma constante y ofrecemos capacitación a las empresas.</h5>", unsafe_allow_html=True)



if selected== "Aplicación":
    margin()
    st.markdown("<h1 style='text-align: center; color: purple;'>Ingresa el comentario a clasificar en la cajita de abajo.</h1>", unsafe_allow_html=True)

    st_lottie(lottie_predict, key="predict",
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        
        height=None,
        width=None,
        ) 



    form = st.form("my_form")
    prompt = form.text_input("Inserta tu comentario aquí:")


        # Now add a submit button to the form:
    if form.form_submit_button("Mostrar resultado"):
        request_text = f"http://127.0.0.1:8000/predict?prompt=${prompt}"
        response = requests.get(request_text, json=prompt)
        prediction = response.text
        st.success(f"El resultado de tu comentario es: {prediction}")


    









