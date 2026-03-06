import streamlit as st

# --- Page d'accueil avec leçon ---
st.title("📚 Bienvenue dans les leçons mathématiques d'Asma !")

if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# fonction son invisible
def play_success():
    st.markdown(
        """
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-3.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# --- Leçon ---
if not st.session_state.started:

    st.write("""
    Aujourd'hui nous allons apprendre :

    🔹 les petits calculs  
    🔹 reconnaître les formes
    """)

    st.write("🎬 Petite vidéo pour comprendre la leçon")

    st.video("https://youtu.be/0TgLtF3PMOc")

    if st.button("Commencer les exercices"):
        st.session_state.started = True


# --- Exercices ---
if st.session_state.started:

    def next_step(correct):

        if correct:
            st.success("✅ Bravo ! Bonne réponse ! 🎉")
            play_success()
            st.session_state.score += 1

        else:
            st.error("❌ Oups ! Ce n'est pas la bonne réponse.")

        st.session_state.step += 1


    # Question 1
    if st.session_state.step == 1:
        st.write("Question 1 : Combien font 1 + 1 ?")

        r = st.text_input("Ta réponse", key="q1")

        if st.button("Valider", key="b1"):
            next_step(r.strip() == "2")


    # Question 2
    elif st.session_state.step == 2:
        st.write("Question 2 : Combien font 2 + 1 ?")

        r = st.text_input("Ta réponse", key="q2")

        if st.button("Valider", key="b2"):
            next_step(r.strip() == "3")


    # Question 3
    elif st.session_state.step == 3:
        st.write("Question 3 : Combien de côtés a un triangle ?")

        r = st.text_input("Ta réponse", key="q3")

        if st.button("Valider", key="b3"):
            next_step(r.strip() == "3")


    # Question 4
    elif st.session_state.step == 4:
        st.write("Question 4 : Combien de côtés a un carré ?")

        r = st.text_input("Ta réponse", key="q4")

        if st.button("Valider", key="b4"):
            next_step(r.strip() == "4")


    # Fin
    elif st.session_state.step == 5:

        st.subheader("🎉 Exercice terminé !")

        score = st.session_state.score
        st.write(f"Ton score est : {score} /4")

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
