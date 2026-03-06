import streamlit as st

# --- Page d'accueil avec leçon ---
st.title("📚 Bienvenue dans les leçons mathématiques d'Asma !")

if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# Son de réussite
success_sound = "https://www.soundjay.com/buttons/sounds/button-3.mp3"

# Texte de la leçon
if not st.session_state.started:
    st.write("""
    Aujourd'hui, nous allons apprendre **les additions et soustractions simples** ainsi que **les formes géométriques**.
    
    🔹 Addition : ajouter des nombres ensemble (ex : 2 + 3 = 5)  
    🔹 Soustraction : enlever des nombres (ex : 5 - 2 = 3)  
    🔹 Formes : triangle = 3 côtés, carré = 4 côtés
    
    Quand tu es prêt, clique sur le bouton pour commencer les exercices !
    """)

    # 🎬 Vidéo explicative
   
