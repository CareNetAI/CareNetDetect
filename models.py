import time
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def tuberculosis_page():

    # model = tf.keras.models.load_model("models/tuberculosis_model.hdf5")
    # class_names = ['Normal', 'Tuberculosis']

    @st.cache_data()
    def preprocess_and_predict(image_file):
        img = image.load_img(image_file, target_size=(224, 224))
        img = image.img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        prediction = model.predict(img)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = round(100   * np.max(prediction), 2)
        return predicted_class, confidence


    st.title("Tuberculosis Detection System")

    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        predict_button = st.button("ㅤㅤPredictㅤㅤ")
    
        if predict_button:
            model = tf.keras.models.load_model("models/tuberculosis_model.hdf5")

            class_names = ['Normal', 'Tuberculosis']

            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.022)
                my_bar.progress(percent_complete + 1, text=progress_text)

            predicted_class, confidence = preprocess_and_predict(uploaded_file)

            st.write(f"Predicted Class: **{predicted_class}**")
            st.write(f"Confidence: {confidence}%")
            

def pneumonia_page():    

    # model = tf.keras.models.load_model('models/pneumonia_model.h5')
    # class_labels = ['Normal', 'Pneumonia']

    @st.cache_data()
    def preprocess_and_predict(image_file):
        img = image.load_img(image_file, color_mode='grayscale', target_size=(256, 256))
        img_array = image.img_to_array(img)
        
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0 

        pred = model.predict(img_array)
        predicted_class = class_labels[int(np.round(pred))]
        return predicted_class

    st.title("Pneumonia Detection System")

    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        model = tf.keras.models.load_model('models/pneumonia_model.h5')

        class_labels = ['Normal', 'Pneumonia']

        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        predict_button = st.button("ㅤㅤPredictㅤㅤ")
        
        if predict_button:
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.022)
                my_bar.progress(percent_complete + 1, text=progress_text)

            predicted_label = preprocess_and_predict(uploaded_file)

            if predicted_label=="Normal":
                st.success("Normal")
                
            elif predicted_label=="Pneumonia":
                st.error("Pneumonia")


def cancer_page():

    # model = tf.keras.models.load_model('models/cancer_model.h5')
    # class_labels = ['Benign', 'Malignant', 'Normal']

    @st.cache_data()
    def preprocess_and_predict(image_file):

        img = image.load_img(image_file, color_mode='grayscale', target_size=(256, 256))
        img_array = image.img_to_array(img)

        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0 

        pred = model.predict(img_array)

        temp = np.array(np.round(pred)).tolist()

        return class_labels[temp[0].index(float(1))]
    
    
    st.title("Cancer Detection System")

    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("")
    
        predict_button = st.button("ㅤㅤPredictㅤㅤ")
    
        if predict_button:

            model = tf.keras.models.load_model('models/cancer_model.h5')

            class_labels = ['Benign', 'Malignant', 'Normal']
    
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.022)
                my_bar.progress(percent_complete + 1, text=progress_text)

            predicted_class = preprocess_and_predict(uploaded_file)

            if predicted_class=="Normal":
                st.success("Normal")
            
            elif predicted_class=="Benign":
                st.warning("Benign")
            
            elif predicted_class=="Malignant":
                st.error("Malignant")