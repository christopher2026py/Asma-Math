# Jeu éducatif : Les fractions
# Niveau primaire (inspiré du système québécois)

score = 0

print("🍕 Bienvenue dans la Pizzeria des Fractions !")
print("Réponds aux questions pour gagner des points.\n")

# Niveau 1
print("Niveau 1 : Comprendre les fractions")

reponse = input("Tu manges 2 parts sur 6 parts de pizza. Quelle est la fraction ? ")

if reponse == "2/6":
    print("✅ Bravo !")
    score += 1
else:
    print("❌ Mauvaise réponse. La bonne réponse est 2/6")

print()

# Niveau 2
print("Niveau 2 : Numérateur et dénominateur")

reponse = input("Dans la fraction 3/5, quel est le numérateur ? ")

if reponse == "3":
    print("✅ Correct !")
    score += 1
else:
    print("❌ Faux. Le numérateur est 3")

reponse = input("Dans la fraction 3/5, quel est le dénominateur ? ")

if reponse == "5":
    print("✅ Correct !")
    score += 1
else:
    print("❌ Faux. Le dénominateur est 5")

print()

# Niveau 3
print("Niveau 3 : Fractions équivalentes")

reponse = input("Complète : 1/3 = ?/6 : ")

if reponse == "2":
    print("✅ Bravo !")
    score += 1
else:
    print("❌ Faux. La réponse est 2 (2/6)")

print()

# Niveau 4
print("Niveau 4 : Mission chocolat 🍫")

reponse = input("Un chocolat a 8 morceaux. Tu manges 3 morceaux. Quelle fraction as-tu mangée ? ")

if reponse == "3/8":
    print("✅ Correct !")
    score += 1
else:
    print("❌ Faux. La réponse est 3/8")

reponse = input("Combien reste-t-il ? (écris la fraction) ")

if reponse == "5/8":
    print("✅ Bien joué !")
    score += 1
else:
    print("❌ Faux. Il reste 5/8")

print()

# Mini jeu vrai ou faux
print("⚡ Mini jeu : Vrai ou Faux")

reponse = input("2/4 = 1/2 (vrai/faux) : ")

if reponse.lower() == "vrai":
    print("✅ Correct !")
    score += 1
else:
    print("❌ Faux. C'était vrai")

reponse = input("3/5 = 5/3 (vrai/faux) : ")

if reponse.lower() == "faux":
    print("✅ Correct !")
    score += 1
else:
    print("❌ Faux. C'était faux")

print("\n🎉 Jeu terminé !")
print("Ton score est :", score, "/7")

if score == 7:
    print("🏆 Excellent ! Tu es un champion des fractions !")
elif score >= 4:
    print("👍 Bon travail ! Continue à pratiquer.")
else:
    print("📚 Continue à t'entraîner, tu vas progresser !")