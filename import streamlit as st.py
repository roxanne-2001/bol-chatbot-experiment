import Groq

client = Groq()

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Vertel iets interessants over UX design."}
    ],
    temperature=0.7,
    max_completion_tokens=512,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")