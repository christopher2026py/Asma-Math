import streamlit as st

# --- Page d'accueil avec leçon ---
st.title("📚 Bienvenue dans les leçons mathématiques d'Asma !")

if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# Texte de la leçon
if not st.session_state.started:
    st.write("""
    Aujourd'hui, nous allons apprendre **les additions et soustractions simples** ainsi que **les formes géométriques**.
    
    🔹 Addition : ajouter des nombres ensemble (ex : 2 + 3 = 5)  
    🔹 Soustraction : enlever des nombres (ex : 5 - 2 = 3)  
    🔹 Formes : triangle = 3 côtés, carré = 4 côtés
    
    Quand tu es prêt, clique sur le bouton pour commencer les exercices !
    """)
    if st.button("Commencer les exercices"):
        st.session_state.started = True

# --- Exercices simples ---
if st.session_state.started:
    def next_step(correct):
        if correct:
            st.session_state.score += 1
        st.session_state.step += 1

    # Question 1
    if st.session_state.step == 1:
        st.write("Question 1 : 2 + 3 = ?")
        reponse = st.text_input("Écris ta réponse", key="q1")
        if st.button("Valider", key="b1"):
            next_step(reponse.strip() == "5")

    # Question 2
    elif st.session_state.step == 2:
        st.write("Question 2 : 5 - 2 = ?")
        reponse = st.text_input("Écris ta réponse", key="q2")
        if st.button("Valider", key="b2"):
            next_step(reponse.strip() == "3")

    # Question 3
    elif st.session_state.step == 3:
        st.write("Question 3 : Combien de côtés a un triangle ?")
        reponse = st.text_input("Écris ta réponse", key="q3")
        if st.button("Valider", key="b3"):
            next_step(reponse.strip() == "3")

    # Question 4
    elif st.session_state.step == 4:
        st.write("Question 4 : Combien de côtés a un carré ?")
        reponse = st.text_input("Écris ta réponse", key="q4")
        if st.button("Valider", key="b4"):
            next_step(reponse.strip() == "4")

    # Fin du jeu
    elif st.session_state.step == 5:
        st.subheader("🎉 Exercice terminé !")
        st.write(f"Ton score est : {st.session_state.score} /4")
        if st.session_state.score == 4:
            st.success("🏆 Parfait ! Tu es un champion !")
        elif st.session_state.score >= 2:
            st.info("👍 Bien joué ! Continue à pratiquer.")
        else:
            st.warning("📚 Continue à t'entraîner !")
        if st.button("Rejouer"):
            st.session_state.started = False
            st.session_state.step = 1
            st.session_state.score = 0
