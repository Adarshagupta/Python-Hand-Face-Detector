import openai

# Set your OpenAI GPT-3 API key here
openai.api_key = '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'

def ask_gpt3(question):
    prompt = f"Question: {question}\nAnswer:"
    
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if needed
        prompt=prompt,
        max_tokens=150,  # Adjust max tokens based on your preference
        temperature=0.7  # Adjust temperature for randomness (0.0 to 1.0)
    )
    
    answer = response.choices[0].text.strip()
    return answer

# Example usage
user_question = input("Ask a question: ")
answer_from_gpt3 = ask_gpt3(user_question)

print(f"Answer: {answer_from_gpt3}")
