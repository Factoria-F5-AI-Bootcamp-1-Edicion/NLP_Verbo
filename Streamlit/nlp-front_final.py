#Importación librerias
import streamlit as st
import warnings
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie


warnings.filterwarnings("ignore")
  
#Lottie Animaciones
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Se ingresa el link de la animacion 
lottie_url_predict = "https://assets8.lottiefiles.com/packages/lf20_D0HSc9DlfZ.json"

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
        # Tipo de menu sidebar 
        with st.sidebar:
            
            selected = option_menu(
                menu_title="Menú",  # requerido
                options=["Página principal","Prediccion","Predicción Youtube"],  # requerido
                icons=["house", "heart", 'heart'],  # opcional
                #menu_icon= "cast",  # opcional
                default_index=0,  # opcional
                styles={
                    "menu-icon":"Data",
                    
                    "menu_title":{"font-family": "Tahoma"},
                    "nav-link": {"font-family": "Tahoma", "text-align": "left", "margin":"0px",},
                    #"nav-link-selected": {""}, 
                    })
        return selected



selected = streamlit_menu(example=EXAMPLE_NO)

# Pagina principal
if selected == "Página principal":

    st.markdown("<h1 style='text-align: center; color: purple;'>DeepIA Tech</h1>", unsafe_allow_html=True)
   
    container = st.container()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
#Se sube el logo y se centra
    with col2:
        st.image("Healthy.png")

    with col3:
        st.write(' ')
    
    
    st.markdown("<h5 style='text-align: justify; color: black;'>DeepIA Tech es una consultoría en la que nos encargamos de buscar soluciones tecnológicas. Nuestro equipo está conformado por data analystics, desarrolladores de Inteligencia Artificial y especialistas en marketing y diseño web.</h5>", unsafe_allow_html=True)

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")

    col1, col2, col3 = st.columns(3)

    with col1:
       st.image("./twiter_logo.png")

    with col2:
       st.image("./instagram_logo.png")

    with col3:
       st.image("./youtube_logo.png")

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")
#Descripcion de la empresa
    st.markdown("<h5 style='text-align: justify'>Así nace Healthy Comments es una aplicación para el análisis de comentarios, como en las redes sociales, que nos ayuda a identificar si son tóxicos o no, utilizando Machine Learning. Queremos seguir desarrollando nuestra herramienta  para que sea mas polivalente e incluso llegar a poder restringir de manera automática los comentarios nocivos hacia otras personas.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify'>Contamos con soporte técnico que ayuda a mantener la herramienta de forma constante y ofrecemos capacitación a las empresas.</h5>", unsafe_allow_html=True)

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")
    st.image("./BigML-Dataset.png")

#Paginas 
if selected== "Prediccion":
    
    margin()


    st.markdown("<h1 style='text-align: center; color: purple;'>Healthy comments</h1>", unsafe_allow_html=True)

    container = st.container()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:

        st_lottie(lottie_predict, key="predict",
        speed=2,
        reverse=True,
        loop=True,
        quality="low", # medium ; high
        
        height=200,
        width=200,
        ) 

    

    form = st.form("my_form")
    prompt = form.text_area("Inserta tu comentario aquí:")



        # Conexion con la API
    if form.form_submit_button("Mostrar resultado"):
        request_text = f"http://127.0.0.1:8000/predict?prompt=${prompt}"
        response = requests.get(request_text, json=prompt)
        prediction = response.text
        st.success(f"El resultado de tu comentario es: {prediction}")
    
if selected== "Predicción Youtube":

    st.markdown("<h1 style='text-align: center; color: purple;'>Healthy comments</h1>", unsafe_allow_html=True)

    container = st.container()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:

            st_lottie(lottie_predict, key="predict",
            speed=2,
            reverse=True,
            loop=True,
            quality="low", # medium ; high
            
            height=200,
            width=200,
            ) 


        #Youtube Scrapper
            form2 = st.form("Comentario Youtube")
            youtube_videoId = form2.text_input("Comentarios de vídeo de Youtube")
            print(type(youtube_videoId))


    # Conexión con la api:
            if form2.form_submit_button("Mostrar resultado"):
                request_text2 = f"http://127.0.0.1:8000/predict_youtube_comment?prompt={youtube_videoId}"
                print(request_text2)
                response2 = requests.get(request_text2)
                prediction2 = response2.text
                st.success(f"El resultado de tu comentario es: {prediction2}")

    









