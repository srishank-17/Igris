from openai import OpenAI

client = OpenAI(api_key="
def get_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return "Error: " + str(e)
