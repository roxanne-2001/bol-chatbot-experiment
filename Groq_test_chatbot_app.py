from groq import Groq

# Zet je echte key hier
client = Groq(api_key="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")

print("Welkom bij je Groq chatbot! Typ 'exit' om te stoppen.\n")

while True:
    user_input = input("Jij: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chat afgesloten. Tot de volgende keer!")
        break

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Je bent een behulpzame AI assistent."},
            {"role": "user", "content": user_input}
        ],
        model="llama-3.3-70b-versatile",
    )

    # Print het antwoord van de AI
    print("AI:", response.choices[0].message.content)