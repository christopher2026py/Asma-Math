import streamlit as st

# --- Page d'accueil avec leçon ---
st.title("📚 Bienvenue dans les leçons mathématiques d'Asma !")

if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# son réussite
success_sound = "https://www.soundjay.com/buttons/sounds/button-3.mp3"

# Texte de la leçon
if not st.session_state.started:

    st.write("""
    Aujourd'hui, nous allons apprendre **les additions et soustractions simples** ainsi que **les formes géométriques**.
    
    🔹 Addition : ajouter des nombres ensemble (ex : 2 + 3 = 5)  
    🔹 Soustraction : enlever des nombres (ex : 5 - 2 = 3)  
    🔹 Formes : triangle = 3 côtés, carré = 4 côtés
    """)

    st.write("🎬 Regarde la vidéo pour comprendre la leçon :")

    # vidéo
    st.video("https://www.youtube.com/watch?v=8NQkY2K0c8Y")

    # bouton
    if st.button("Commencer les exercices"):
        st.session_state.started = True


# --- Exercices simples ---
if st.session_state.started:

    def next_step(correct):
        if correct:
            st.session_state.score += 1
            st.audio(success_sound)
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

        score = st.session_state.score
        st.write(f"Ton score est : {score} /4")

        # étoiles
        stars = "⭐" * score
        st.write("Tes étoiles :", stars)

        if score == 4:
            st.success("🏆 Parfait ! Tu es un champion !")
            st.balloons()

        elif score >= 2:
            st.info("👍 Bien joué ! Continue à pratiquer.")

        else:
            st.warning("📚 Continue à t'entraîner !")

        if st.button("Rejouer"):
            st.session_state.started = False
            st.session_state.step = 1
            st.session_state.score = 0
