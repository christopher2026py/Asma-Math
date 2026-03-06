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

# --- Exercices interactifs ---
if st.session_state.started:
    def next_step(correct):
        if correct:
            st.session_state.score += 1
            st.success("✅ Correct ! 🎉")
        else:
            st.error("❌ Mauvaise réponse")
        st.session_state.step += 1

    total_questions = 4
    st.write(f"Tu es à la question {st.session_state.step} sur {total_questions}")

    # Question 1
    if st.session_state.step == 1:
        st.write("Question 1 : 2 + 3 = ?")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("4"):
                next_step(False)
        with col2:
            if st.button("5"):
                next_step(True)
        with col3:
            if st.button("6"):
                next_step(False)

    # Question 2
    elif st.session_state.step == 2:
        st.write("Question 2 : 5 - 2 = ?")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("2"):
                next_step(False)
        with col2:
            if st.button("3"):
                next_step(True)
        with col3:
            if st.button("4"):
                next_step(False)

    # Question 3
    elif st.session_state.step == 3:
        st.write("Question 3 : Combien de côtés a un triangle ?")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("3"):
                next_step(True)
        with col2:
            if st.button("4"):
                next_step(False)
        with col3:
            if st.button("5"):
                next_step(False)

    # Question 4
    elif st.session_state.step == 4:
        st.write("Question 4 : Combien de côtés a un carré ?")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("3"):
                next_step(False)
        with col2:
            if st.button("4"):
                next_step(True)
        with col3:
            if st.button("5"):
                next_step(False)

    # Fin du jeu
    elif st.session_state.step == 5:
        st.subheader("🎉 Exercice terminé !")
        st.write(f"Ton score est : {st.session_state.score} /{total_questions}")

        # Affichage étoiles
        st.write("⭐" * st.session_state.score + "☆" * (total_questions - st.session_state.score))

        if st.session_state.score == total_questions:
            st.balloons()
            st.success("🏆 Parfait ! Tu es un champion !")
        elif st.session_state.score >= total_questions/2:
            st.info("👍 Bien joué ! Continue à pratiquer.")
        else:
            st.warning("📚 Continue à t'entraîner !")

        if st.button("Rejouer"):
            st.session_state.started = False
            st.session_state.step = 1
            st.session_state.score = 0
