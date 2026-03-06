import streamlit as st

st.title("📚 Bienvenue dans les leçons mathématiques d'Asma !")

if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "correct" not in st.session_state:
    st.session_state.correct = False


# son invisible
def play_success():
    st.markdown(
        """
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-09.mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )


# -------- LEÇON --------

if not st.session_state.started:

    st.write("""
Aujourd'hui nous allons apprendre :

🔹 les petits calculs  
🔹 reconnaître les formes
""")

    st.video("https://youtu.be/0TgLtF3PMOc")

    if st.button("Commencer les exercices"):
        st.session_state.started = True
        st.rerun()


# -------- EXERCICES --------

if st.session_state.started:

    questions = [
        ("Combien font 1 + 1 ?", "2"),
        ("Combien font 2 + 1 ?", "3"),
        ("Combien de côtés a un triangle ?", "3"),
        ("Combien de côtés a un carré ?", "4"),
    ]

    if st.session_state.step <= len(questions):

        question, bonne = questions[st.session_state.step - 1]

        st.write(f"Question {st.session_state.step} : {question}")

        if not st.session_state.answered:

            r = st.text_input("Ta réponse")

            if st.button("Valider"):

                st.session_state.correct = (r.strip() == bonne)

                if st.session_state.correct:
                    st.session_state.score += 1

                st.session_state.answered = True
                st.rerun()

        else:

            if st.session_state.correct:
                st.success("✅ Bravo ! Bonne réponse ! 🎉")
                play_success()
            else:
                st.error("❌ Ce n'est pas la bonne réponse.")

            if st.button("Question suivante"):
                st.session_state.step += 1
                st.session_state.answered = False
                st.rerun()


    else:

        st.subheader("🎉 Exercice terminé !")

        score = st.session_state.score

        st.write(f"Ton score est : {score} /4")

        st.write("Tes étoiles :", "⭐" * score)

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
            st.session_state.answered = False
            st.rerun()
