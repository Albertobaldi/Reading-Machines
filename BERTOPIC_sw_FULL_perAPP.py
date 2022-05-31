import streamlit as st
import pandas as pd
import numpy as np
import base64
import warnings
warnings.filterwarnings("ignore")
import re
from tqdm import tqdm
import string
import nltk
import io
from io import StringIO
import string
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bertopic import BERTopic

from nltk.corpus import stopwords
stopwords = stopwords.words('italian')

st.set_page_config(
    page_title="BERTopic",
    page_icon="🎈",
) 

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )
    
def get_topic_model(lines):
    topic_model = BERTopic(language="multilingual", calculate_probabilities=True, verbose=True)
    topics, probs = topic_model.fit_transform(lines)
    freq = topic_model.get_topic_info(); freq.head(5)
    return topics, freq, topic_model
    
def topic_model_visualize(topic_model):
    return topic_model.visualize_topics()

def topic_model_distribution(topic_model):
    return topic_model.visualize_distribution(probs[200], min_probability=0.015)

def topic_model_hierarchy(topic_model):
    return topic_model.visualize_hierarchy(top_n_topics=50)

def topic_model_barchart(topic_model):
    return topic_model.visualize_barchart(top_n_topics=5)
    
df = None
uploaded_file = st.sidebar.file_uploader('Carica un file .txt')
st.sidebar.caption('Verifica che il file sia privo di formattazione')
st.sidebar.markdown("""---""")
if df is not None:
    with open(df, 'r', encoding='utf-8') as f:
        lines = f.readlines()    
        
if st.button('Esegui l’analisi'):
    tm_state = st.text('Modeling topics...')
    text, dates, topic_model, topics = get_topic_model(lines)
    tm_state.text('Modeling topics... done!')
    
    with st.container():
        st.write("This is inside the container")

        fig1 = topic_model_visualize(topic_model)
        st.write(fig1)
        fig2 = topic_model_distribution(topic_model)
        st.write(fig2)
        fig3 = topic_model_hierarchy(topic_model)
        st.write(fig3)
        fig4 = topic_model_barchart(topic_model)
        st.write(fig4)
