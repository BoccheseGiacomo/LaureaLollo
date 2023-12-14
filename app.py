import streamlit as st

# Titolo del quiz
st.title("Quiz per Lollo: Barcollo ma non mollo")

# Domande del quiz
quiz_questions = {
    "π =": (["Scegli una risposta", "3.14", "π", "3", "e^2"], "3"),
    "g =": (["Scegli una risposta", "9.81", "g", "e^2"], "e^2"),
    "Come si pronuncia la parola \"GAUGE\"?": (["Scegli una risposta", "gheig", "goge", "gauge"], "gauge"),
    "ε (epsilon) uguale:": (["Scegli una risposta", "0", "0.01", "1"], "0"),
    "Risolvi il seguente problema: Fratta lancia da un grattacielo nel vuoto una piuma e un mattone, cosa tocca terra per primo?": (
        ["Scegli una risposta", "La piuma", "Il mattone", "Nessuno perché nel vuoto non c'è gravità", "Fratta perché è un mattone"], "Fratta perché è un mattone"),
    "Semplifica questa espressione: (vedi sotto)": (["Scegli una risposta", "100", "0", "g"], "100")
}

# Memorizza le risposte dell'utente
user_answers = {}

# Rendering delle domande e delle opzioni
for question, (options, correct_answer) in quiz_questions.items():
    # Imposta la scelta predefinita sulla prima opzione che è il placeholder
    user_answers[question] = st.radio(question, options, index=0)

# Renderizzare l'espressione LaTeX separatamente
st.latex(r"(\pi^2 - 3e^2 + 2ge) \cdot \varepsilon + g^2")


# Bottone per inviare le risposte
if st.button("Verifica"):
    # Controlla se tutte le domande hanno una risposta e che la risposta non sia il placeholder
    all_answered = all(answer != "Scegli una risposta" for answer in user_answers.values())
    if all_answered:
        # Calcolo del punteggio
        score = sum(user_answers[q] == correct_answer for q, (options, correct_answer) in quiz_questions.items())
        total_questions = len(quiz_questions)
        percentage = round((score / total_questions) * 100)  # Calcolo della percentuale arrotondata all'unità

        # Personalizzazione del messaggio in base al punteggio con evidenziatura
        if percentage < 40:
            st.markdown(f'<p style="background-color:red;color:white;padding:10px;font-size:20px;">Il tuo punteggio è {percentage}%. Sei peggio di un matematico!</p>', unsafe_allow_html=True)
        elif 40 <= percentage < 70:
            st.markdown(f'<p style="background-color:yellow;color:black;padding:10px;font-size:20px;">Il tuo punteggio è {percentage}%. Si vede che sei un fisico</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="background-color:green;color:white;padding:10px;font-size:20px;">Il tuo punteggio è {percentage}%. Bravo, sei un ingegnere!</p>', unsafe_allow_html=True)
    else:
        st.error("Devi rispondere a tutte le domande.")
