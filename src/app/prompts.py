# src/app/prompts/prompts.py

from .app_types import Mode, Chunk

def system_prompt(mode: Mode) -> str:
    if mode == Mode.STUDY:
        return (
            "You are a helpful BIFS 614 tutor and assistant.\n"
            "Explain concepts clearly, step-by-step.\n"
            "Answer the student's question directly.\n"
            "Provide examples when helpful.\n"
        )
    else:
        # assessment / exam mode
        return (
            "You are a BIFS 614 assessment proctor.\n"
            "Do not provide the full answer or solution.\n"
            "Identify and address the student's knowledge gaps.\n"
            "Encourage the student to explain their reasoning.\n"
        )


def build_context(chunks: list[Chunk]) -> str:
    if not chunks:
        return "No course content found."

 
    lines = ["Course Context:"]
    for i, c in enumerate(chunks, start=1):
        lines.append(
            f"[{i}] ({c.get('source')}) {c.get('text')}"
        )

    return "\n".join(lines)