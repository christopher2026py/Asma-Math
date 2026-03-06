import streamlit as st

st.title("📚 Bienvenue dans les leçons mathématiques d'Asma !")
st.write("Réponds aux questions pour t'amuser et apprendre !")

# Initialiser le score et l'étape
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# Fonction pour passer à la question suivante
def next_step(correct):
    if correct:
        st.session_state.score += 1
    st.session_state.step += 1

# --- Questions CE1 ---
if st.session_state.step == 1:
    st.write("Question 1 : 2 + 3 = ?")
    reponse = st.text_input("Écris ta réponse", key="q1")
    if st.button("Valider", key="b1"):
        next_step(reponse.strip() == "5")

elif st.session_state.step == 2:
    st.write("Question 2 : 5 - 2 = ?")
    reponse = st.text_input("Écris ta réponse", key="q2")
    if st.button("Valider", key="b2"):
        next_step(reponse.strip() == "3")

elif st.session_state.step == 3:
    st.write("Question 3 : Combien de côtés a un triangle ?")
    reponse = st.text_input("Écris ta réponse", key="q3")
    if st.button("Valider", key="b3"):
        next_step(reponse.strip() == "3")

elif st.session_state.step == 4:
    st.write("Question 4 : Quelle couleur obtient-on en mélangeant bleu et jaune ?")
    reponse = st.text_input("Écris ta réponse", key="q4")
    if st.button("Valider", key="b4"):
        next_step(reponse.strip().lower() == "vert")

elif st.session_state.step == 5:
    st.subheader("🎉 Jeu terminé !")
    st.write(f"Ton score est : {st.session_state.score} /4")
    if st.session_state.score == 4:
        st.success("🏆 Parfait ! Tu es un champion !")
    elif st.session_state.score >= 2:
        st.info("👍 Bien joué ! Continue à pratiquer.")
    else:
        st.warning("📚 Continue à t'entraîner !")
    if st.button("Rejouer"):
        st.session_state.step = 1
        st.session_state.score = 0
