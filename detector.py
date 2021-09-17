import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
import pandas as pd    
import tensorflow as tf
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from skimage import io

from PIL import Image

BATCH_SIZE=1

def decode_test(name):
  img=tf.io.read_file(name)#lo lee en byts
  img=tf.image.decode_jpeg(img,channels=3)#lo carga como imagen
  img=tf.cast(img,tf.float32)#/255#cambia la presicion
  img = tf.image.resize(img, [224,224])
  return img

def load_test_ds(df):
  imgs=df["image_name"].values#Creo una lista 
  imgs=[f"{name}" for name in imgs]#Creo una lista con mis rutas
  ds=tf.data.Dataset.from_tensor_slices(imgs)
  ds=ds.map(decode_test)
  ds=ds.batch(BATCH_SIZE)
  return ds


def decode_test3(img):
    img =  tf.cast(img,tf.float32)#/255#cambia la presicion
    img =  tf.image.resize(img, [224,224])
    img =  img.batch(BATCH_SIZE)
        #test_ds = tf.reshape(img, [1,224,224,3])
        #test_ds= tf.expand_dims(img, axis=0)
    return img

def load_test_ds3(uploaded_file):
    ds=Image.open(uploaded_file).convert("RGB")
    ds=tf.data.Dataset.from_tensor_slices(ds)
    ds=ds.map(decode_test3)
    ds=ds.batch(1)
    return ds


    
def main():
    st.title('DETECTOR DE MASCARILLAS')
    st.markdown("## Sube una imagen de una persona para detectar si lleva puesta su mascarilla.")
    image1="prueba1.jpg"
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        
        img=np.array(img)#lo carga como imagen
        #img=tf.data.Dataset.range(1)
        #img=img.map(decode_test3)
        img=tf.cast(img,tf.float32)
        img = tf.image.resize(img, [224,224])
        test_ds= tf.expand_dims(img, axis=0)
        #test_ds=tf.TensorShape([None, 224, 224, 3])
        #st.write(test_ds)
        model = load_model('model.h5')
        preds = []

        
        _preds=model.predict(test_ds)
        preds += _preds.ravel().tolist()
        
        submission=pd.DataFrame({
        "id":uploaded_file.name,"label":preds
        })
        submission['target'] = submission['label'].apply(np.round)
            #CON MASCARA=0 SIN MASCARA=1
        submission['target'] =submission["target"].replace({1: "Sin_Tapa_Bocas", 0:"Con_Tapa_Bocas"})

        st.write(submission)
        image5 = Image.open(uploaded_file)
        label=submission["target"].values
        st.image(image5, caption=label)
        if label==['Con_Tapa_Bocas']:
            st.markdown("## LA PERSONA LLEVA EL TAPA BOCAS")
        else:
            st.markdown("## LA PERSONA NO LLEVA EL TAPA BOCAS")

        
    else:


        test_split= pd.DataFrame({"image_name":image1},index=[0])   
        # Modelo de carga
        model = load_model('model.h5')
        test_ds=load_test_ds(test_split)
        preds = []

        for imgs in test_ds:
            imgs_lr=tf.image.flip_left_right(imgs)
            imgs_ud=tf.image.flip_up_down(imgs)
            _preds=model.predict(imgs)
            preds += _preds.ravel().tolist()
        
        submission=pd.DataFrame({
        "id":test_split["image_name"].values,"label":preds
    })
        submission['target'] = submission['label'].apply(np.round)
        #CON MASCARA=0 SIN MASCARA=1
        submission['target'] =submission["target"].replace({1: "Sin_Tapa_Bocas", 0:"Con_Tapa_Bocas"})

        img=io.imread(f"{image1}")
        imgplot =plt.imshow(img)
        plt.axis(False)
        label=submission["target"].values
        plt.title(label)
        plt.show()

        st.write(submission)
        image5 = Image.open('prueba1.jpg')
        st.image(image5, caption=label)
        if label==['Con_Tapa_Bocas']:
            st.markdown("## LA PERSONA LLEVA EL TAPA BOCAS")
        else:
            st.markdown("## LA PERSONA NO LLEVA EL TAPA BOCAS")