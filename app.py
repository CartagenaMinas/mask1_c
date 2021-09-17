####################### Importar Librerias ############################
import streamlit as st
import menu
from PIL import Image
import detector
import post
######################### Funciones #################################
# Set the configs
APP_TITLE = "DETECTOR DE MASCARILLAS"
st.set_page_config(
    page_title = APP_TITLE,
    page_icon = Image.open('utils/pickaxe.png'),
    layout = "centered",
    initial_sidebar_state = "auto")
icon = Image.open('utils/pickaxe.png')


# External CSS
main_external_css = """
    <style>
        hr {margin: 15px 0px !important; background: #ff3a50}
        .footer {position: absolute; height: 50px; bottom: -150px; width:100%; padding:10px; text-align:center; }
        #MainMenu, .reportview-container .main footer {display: none;}
        .btn-outline-secondary {background: #FFF !important}
        .download_link {color: #f63366 !important; text-decoration: none !important; z-index: 99999 !important;
                        cursor:pointer !important; margin: 15px 0px; border: 1px solid #f63366;
                        text-align:center; padding: 8px !important; width: 200px;}
        .download_link:hover {background: #f63366 !important; color: #FFF !important;}
        h1, h2, h3, h4, h5, h6, a, a:visited {color: #054396 !important}
        label, stText, p, .caption {color: #000000 }
        .streamlit-expanderHeader {font-size: 16px !important;}
        .css-17eq0hr label, stText, .caption, .css-j075dz, .css-1t42vg8 {color: #FFF !important}
        .css-17eq0hr a {text-decoration:underline;}
        .tickBarMin, .tickBarMax {color: #f84f57 !important}
        .markdown-text-container p {color: #035672 !important}
        .css-xq1lnh-EmotionIconBase {fill: #ff3a50 !important}
        .css-hi6a2p {max-width: 800px !important}
        /* Tabs */
        .tabs { position: relative; min-height: 200px; clear: both; margin: 40px auto 0px auto; background: #efefef; box-shadow: 0 48px 80px -32px rgba(0,0,0,0.3); }
        .tab {float: left;}
        .tab label { background: #f84f57; cursor: pointer; font-weight: bold; font-size: 18px; padding: 10px; color: #fff; transition: background 0.1s, color 0.1s; margin-left: -1px; position: relative; left: 1px; top: -29px; z-index: 2; }
        .tab label:hover {background: #035672;}
        .tab [type=radio] { display: none; }
        .content { position: absolute; top: -1px; left: 0; background: #fff; right: 0; bottom: 0; padding: 30px 20px; transition: opacity .1s linear; opacity: 0; }
        [type=radio]:checked ~ label { background: #035672; color: #fff;}
        [type=radio]:checked ~ label ~ .content { z-index: 1; opacity: 1; }
        /* Feature Importance Plotly Link Color */
        .js-plotly-plot .plotly svg a {color: #f84f57 !important}
    </style>
"""
st.markdown(main_external_css, unsafe_allow_html=True)





###################### SiderBar ########################################
st.sidebar.title('DEEP LEARNING PARA CLASIFICACIÓN EN IMÁGENES')
st.sidebar.markdown("<div style='text-align: justify'>Esta app está enfocada a ser de guía básica de cómo utilizar Deep Learning para clasificar si una persona lleva mascarilla o no lleva mascarilla.</div>", unsafe_allow_html=True)
st.sidebar.title('Menú de opciones')
options = st.sidebar.radio('Seleccione una página:', 
    ['DETECTOR DE MASCARILLAS','CODIGO',"INFORMACIÓN"])



#################### Lista de Menus ###################
if options == 'DETECTOR DE MASCARILLAS':
    detector.main()
elif options == 'CODIGO':
    post.main()
elif options == 'INFORMACIÓN':
    menu.principal()