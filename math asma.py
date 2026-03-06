import streamlit as st

st.title("🍕 Bienvenue dans la Pizzeria des Fractions !")
st.write("Réponds aux questions pour gagner des points.\n")

score = 0

# --- Niveau 1 ---
st.subheader("Niveau 1 : Comprendre les fractions")
reponse1 = st.text_input("Tu manges 2 parts sur 6 parts de pizza. Quelle est la fraction ?", key="q1")
if reponse1:
    if reponse1.strip() == "2/6":
        st.success("✅ Bravo !")
        score += 1
    else:
        st.error("❌ Mauvaise réponse. La bonne réponse est 2/6")

# --- Niveau 2 ---
st.subheader("Niveau 2 : Numérateur et dénominateur")
reponse2 = st.text_input("Dans la fraction 3/5, quel est le numérateur ?", key="q2")
if reponse2:
    if reponse2.strip() == "3":
        st.success("✅ Correct !")
        score += 1
    else:
        st.error("❌ Faux. Le numérateur est 3")

reponse3 = st.text_input("Dans la fraction 3/5, quel est le dénominateur ?", key="q3")
if reponse3:
    if reponse3.strip() == "5":
        st.success("✅ Correct !")
        score += 1
    else:
        st.error("❌ Faux. Le dénominateur est 5")

# --- Niveau 3 ---
st.subheader("Niveau 3 : Fractions équivalentes")
reponse4 = st.text_input("Complète : 1/3 = ?/6", key="q4")
if reponse4:
    if reponse4.strip() == "2":
        st.success("✅ Bravo !")
        score += 1
    else:
        st.error("❌ Faux. La réponse est 2 (2/6)")

# --- Niveau 4 ---
st.subheader("Niveau 4 : Mission chocolat 🍫")
reponse5 = st.text_input("Un chocolat a 8 morceaux. Tu manges 3 morceaux. Quelle fraction as-tu mangée ?", key="q5")
if reponse5:
    if reponse5.strip() == "3/8":
        st.success("✅ Correct !")
        score += 1
    else:
        st.error("❌ Faux. La réponse est 3/8")

reponse6 = st.text_input("Combien reste-t-il ? (écris la fraction)", key="q6")
if reponse6:
    if reponse6.strip() == "5/8":
        st.success("✅ Bien joué !")
        score += 1
    else:
        st.error("❌ Faux. Il reste 5/8")

# --- Mini jeu vrai ou faux ---
st.subheader("⚡ Mini jeu : Vrai ou Faux")
reponse7 = st.radio("2/4 = 1/2", ("vrai", "faux"), key="q7")
if reponse7:
    if reponse7.lower() == "vrai":
        st.success("✅ Correct !")
        score += 1
    else:
        st.error("❌ Faux. C'était vrai")

reponse8 = st.radio("3/5 = 5/3", ("vrai", "faux"), key="q8")
if reponse8:
    if reponse8.lower() == "faux":
        st.success("✅ Correct !")
        score += 1
    else:
        st.error("❌ Faux. C'était faux")

# --- Score final ---
st.subheader("🎉 Jeu terminé !")
st.write(f"Ton score est : {score} /7")

if score == 7:
    st.balloons()
    st.success("🏆 Excellent ! Tu es un champion des fractions !")
elif score >= 4:
    st.info("👍 Bon travail ! Continue à pratiquer.")
else:
    st.warning("📚 Continue à t'entraîner, tu vas progresser !")
