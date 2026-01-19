import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from sklearn.ensemble import IsolationForest
import numpy as np

@st.cache_data
def įkelti_duomenis():
    failo_kelias = 'C:/Users/alexm/Downloads/MKA_sudeties_tyrimai_2024.xlsx'
    santraukos_df = pd.read_excel(failo_kelias, sheet_name='1 priedas (apibendrinta)', header=4)
    santraukos_df.columns = ['Eil. Nr.', 'Rūšys', 'tuščias'] + ['Vilniaus', 'Kauno', 'Klaipėdos', 'Panevėžio', 'Šiaulių', 'Marijampolės', 'Alytaus', 'Tauragės', 'Utenos', 'Telšių', 'Vidutiniškai']
    santraukos_df = santraukos_df.drop(columns=['tuščias', 'Eil. Nr.']).dropna(subset=['Rūšys'])
    
    detalaus_df = pd.read_excel(failo_kelias, sheet_name='1 priedas (detali)', header=4)
    detalaus_df.columns = ['Regionai', 'tuščias1', 'Savivaldybės', 'Eil. Nr.', 'Rūšys', 'tuščias2', 'PAVASARIS', 'VASARA', 'RUDUO', 'ŽIEMA', 'BENDRAS']
    detalaus_df = detalaus_df.drop(columns=['tuščias1', 'tuščias2', 'Eil. Nr.']).dropna(subset=['Rūšys'])
    
    return santraukos_df, detalaus_df

santraukos_df, detalaus_df = įkelti_duomenis()

modelis = SentenceTransformer('paraphrase-MiniLM-L6-v2') 

@st.cache_data
def generuoti_aprašymus(df):
    aprašymai = []
    for _, eilutė in df.iterrows():
        if 'Rūšys' in eilutė:
            rūšys = eilutė['Rūšys']
            if 'Vidutiniškai' in eilutė:
                vid = eilutė['Vidutiniškai']
                apraš = f"Vidutinis {rūšys} procentas visose regionuose yra {vid}%."
                aprašymai.append(apraš)
            else:
                for regionas in ['Vilniaus', 'Kauno', 'Klaipėdos', 'Panevėžio', 'Šiaulių', 'Marijampolės', 'Alytaus', 'Tauragės', 'Utenos', 'Telšių']:
                    if regionas in eilutė and pd.notna(eilutė[regionas]):
                        proc = eilutė[regionas]
                        apraš = f"{regionas} regione {rūšys} procentas yra {proc}%."
                        aprašymai.append(apraš)
    return aprašymai

santraukos_aprašymai = generuoti_aprašymus(santraukos_df)

įterpiniai = modelis.encode(santraukos_aprašymai)

def atsakyti_klausimą(užklausa):
    užklausos_įterp = modelis.encode(užklausa)
    panašumai = util.cos_sim(užklausos_įterp, įterpiniai)[0]
    top_ind = np.argmax(panašumai)
    if panašumai[top_ind] > 0.5:  
        return santraukos_aprašymai[top_ind]
    else:
        return "Nerasta susijusios informacijos duomenyse."

@st.cache_data
def aptikti_anomalijas(df):

    if 'Regionai' in df.columns:
        df['Regionai'] = df['Regionai'].ffill()
    if 'Savivaldybės' in df.columns:
        df['Savivaldybės'] = df['Savivaldybės'].ffill()
    
    kontekstas = [col for col in ['Regionai', 'Savivaldybės', 'Rūšys'] if col in df.columns]
    
    skaitiniai = [col for col in df.columns 
                  if col not in ['Regionai', 'Savivaldybės', 'Rūšys'] 
                  and pd.api.types.is_numeric_dtype(df[col])]
    
    if len(skaitiniai) == 0:
        return pd.DataFrame()
    
    duomenys = df[skaitiniai].fillna(0).values
    
    izo_mišras = IsolationForest(contamination=0.1, random_state=42)
    prognozės = izo_mišras.fit_predict(duomenys)
    
    rodomi = kontekstas + skaitiniai if kontekstas else skaitiniai
    
    anomalijos = df[prognozės == -1][rodomi].copy()
    
    if 'Savivaldybės' in anomalijos.columns:
        anomalijos = anomalijos[anomalijos['Savivaldybės'].notna() & (anomalijos['Savivaldybės'] != 'None')]
    
    return anomalijos

anomalijos_santrauka = aptikti_anomalijas(santraukos_df)
anomalijos_detalus = aptikti_anomalijas(detalaus_df)

st.title("Lietuvos Atliekų Sudėties Analizatorius")

st.header("Duomenų Apžvalga")
st.dataframe(santraukos_df)

st.header("Užduokite Klausimą apie Duomenis (NLP K&A)")
užklausa = st.text_input("Įveskite klausimą (pvz., 'Koks vidutinis popieriaus atliekų procentas?')")
if užklausa:
    atsakymas = atsakyti_klausimą(užklausa)
    st.write("Atsakymas:", atsakymas)

st.header("Anomalijų Aptikimas Atliekų Duomenyse (ML Modulis)")
st.subheader("Anomalijos Santraukos Duomenyse")
st.dataframe(anomalijos_santrauka)

st.subheader("Anomalijos Detaliuose Duomenyse")
st.dataframe(anomalijos_detalus)