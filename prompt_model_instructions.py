 """
Member 3: Prompt Model Instructions

This module:
- Enforces BIFS 614 answering.
- Builds structured prompts.
- Validates context strength.
- Controls response formatting.
"""

# 1. SYSTEM RULES

SYSTEM_PROMPT = """
You are a BIFS 614 Tutor and Exam Proctor.

Rules:
- Use ONLY the retrieved BIFS 614 lecture chunks.
- Do NOT use outside knowledge.
- If context is insufficient, ask clarifying questions.
- Do not guess.
- Follow the required structured response format.
"""

RESPONSE_FORMAT = """
Format your response as:

1) Answer
2) Explanation (bullet points)
3) Mini-example
4) Quick check question
5) Evidence used (source, chunk_id)
"""

# 2. CONTEXT STRENGTH CHECK

def context_strength(retrieved_chunks):
    """Determines whether retrieved lecture chunks are strong enough to answer the question."""
    if not retrieved_chunks:
        return "NONE"

    # Length check to prevent insufficient context answers.
    if len(retrieved_chunks[0].get("text", "")) < 200:
        return "WEAK"

    return "STRONG"

# 3. BUILD FULL PROMPT

def build_prompt(question, retrieved_chunks):
    """Combines student question and retrieved lecture context into one prompt."""
    context_text = ""

    for chunk in retrieved_chunks:
        source = chunk.get("source", "UNKNOWN_SOURCE")
        chunk_id = chunk.get("chunk_id", "UNKNOWN_ID")
        text = chunk.get("text", "")

        context_text += f"\nSOURCE: {source} | CHUNK_ID: {chunk_id}\n{text}\n"

    full_prompt = f"""
Student Question:
{question}

Retrieved Lecture Context:
{context_text}

{RESPONSE_FORMAT}
"""
    return full_prompt

# 4. GENERATE ANSWER USING OPENAI CLIENT

def generate_answer(question, retrieved_chunks, openai_client):
    """Validates context, builds prompt, and generates a response."""
    strength = context_strength(retrieved_chunks)

    if strength == "NONE":
        return (
            "I do not have enough BIFS 614 lecture context to answer this question. "
            "Please specify the week or topic."
        )

    if strength == "WEAK":
        return (
            "The retrieved lecture material may be insufficient. "
            "Can you clarify the topic or provide more detail?"
        )

    prompt = build_prompt(question, retrieved_chunks)

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2  # lower temperature = less random / more consistent
    )

    return response.choices[0].message.content

# 5. PROMPT TUNING LOOP

def prompt_tuning(test_questions, retriever_function, openai_client):
    """Runs test questions to evaluate clarity and formatting consistency."""
    results = []

    for question in test_questions:
        retrieved = retriever_function(question)
        answer = generate_answer(question, retrieved, openai_client)

        results.append({
            "question": question,
            "answer": answer
        })

    return results
