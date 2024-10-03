from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Kaise ho"}],

)
print(response.choices[0].message.content)
