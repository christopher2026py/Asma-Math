import streamlit as st

st.title("🍕 Pizzeria des Fractions !")

# Initialiser le score et l'étape avec st.session_state
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# Fonction pour passer à la question suivante
def next_step(correct):
    if correct:
        st.session_state.score += 1
    st.session_state.step += 1

# --- Question par question ---
if st.session_state.step == 1:
    st.write("Niveau 1 : Comprendre les fractions")
    reponse = st.text_input("Tu manges 2 parts sur 6 parts de pizza. Quelle est la fraction ?", key="q1")
    if st.button("Valider", key="b1"):
        next_step(reponse.strip() == "2/6")

elif st.session_state.step == 2:
    st.write("Niveau 2 : Numérateur et dénominateur")
    reponse1 = st.text_input("Quel est le numérateur de 3/5 ?", key="q2")
    reponse2 = st.text_input("Quel est le dénominateur de 3/5 ?", key="q3")
    if st.button("Valider", key="b2"):
        next_step(reponse1.strip() == "3" and reponse2.strip() == "5")

elif st.session_state.step == 3:
    st.write("Niveau 3 : Fractions équivalentes")
    reponse = st.text_input("Complète : 1/3 = ?/6", key="q4")
    if st.button("Valider", key="b3"):
        next_step(reponse.strip() == "2")

elif st.session_state.step == 4:
    st.write("Niveau 4 : Mission chocolat 🍫")
    reponse1 = st.text_input("Tu manges 3 morceaux sur 8, quelle fraction as-tu mangée ?", key="q5")
    reponse2 = st.text_input("Combien reste-t-il ?", key="q6")
    if st.button("Valider", key="b4"):
        next_step(reponse1.strip() == "3/8" and reponse2.strip() == "5/8")

elif st.session_state.step == 5:
    st.write("Mini jeu : Vrai ou Faux")
    reponse1 = st.radio("2/4 = 1/2", ("vrai", "faux"), key="q7")
    reponse2 = st.radio("3/5 = 5/3", ("vrai", "faux"), key="q8")
    if st.button("Valider", key="b5"):
        next_step(reponse1 == "vrai" and reponse2 == "faux")

elif st.session_state.step == 6:
    st.subheader("🎉 Jeu terminé !")
    st.write(f"Ton score est : {st.session_state.score} /7")
    if st.session_state.score == 7:
        st.balloons()
        st.success("🏆 Excellent ! Tu es un champion des fractions !")
    elif st.session_state.score >= 4:
        st.info("👍 Bon travail ! Continue à pratiquer.")
    else:
        st.warning("📚 Continue à t'entraîner, tu vas progresser !")
    if st.button("Rejouer"):
        st.session_state.step = 1
        st.session_state.score = 0
