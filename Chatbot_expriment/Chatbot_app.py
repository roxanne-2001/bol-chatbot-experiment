import openai

openai.api_key = "YOUR_API_KEY_HERE"

def vraag_chatbot(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content

try:
    import openai
    openai.api_key = "YOUR_API_KEY_HERE"
    def vraag_chatbot(prompt):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content
except ImportError:
    def vraag_chatbot(prompt):
        return "[Simulatie] Dit is een voorbeeldantwoord op je vraag: " + prompt

vraag = "Geef een korte beschrijving van de iPhone 14 op Bol.com"
print(vraag_chatbot(vraag))

# Testvraag
vraag = "Geef een korte beschrijving van de iPhone 14 op Bol.com"
antwoord = vraag_chatbot(vraag)
print(antwoord)