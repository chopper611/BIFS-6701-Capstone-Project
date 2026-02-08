# src/app/prompts.py

from.types.py import Mode, Chunk
def system_prompt(mode: Mode) -> str: 
    if mode == "study"
    return (
        "You are a helpful BIFS 614 tutor and assistant.\n"
        "Explain concepts clearly, step-by step.\n"
        "Answer the student's question directly.\n"
        "Provide examples when helpful.\n"
    )

    #assessment mode 
    return ( 
        "You are a BIFS 614 assessment proctor.\n"
        "Do not provide the full answer or full solution.\n"
        "Identify and address the student's knowledge gaps.\n"
        "Encourage the student to explain their reasoning.\n"
    )


    def build_context(chunks: list[Chunk]) -> str:
        if not chunks:
            return "No course content found."

        lines = ["Course Context:"]
        for i, c in enumerate(chunks, start = 1):
            lines.append(f"[{i}] ({c.source}) ({c.text})")
            return "\n".join(lines)