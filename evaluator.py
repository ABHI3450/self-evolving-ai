def evaluate_answer(question, answer, ask_ai_func):

    prompt = f"""
You are an expert reviewer.

Question: {question}
Answer: {answer}

Give:
1) Score (1-10)
2) Short feedback

Format:
Score: X
Feedback: ...
"""

    review = ask_ai_func(prompt)

    return review
