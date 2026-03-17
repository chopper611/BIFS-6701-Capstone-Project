#src/app/main.py

import argparse
import json
import sys
from typing import Optional

from .types import Mode, AppResponse
from .basic_retrieval import BasicRetriever
from .llm_client import LLM_Client
from .orchestrator import Orchestrator


def parse_mode(text: Optional[str]) -> Mode:
    if not text:
        return Mode.STUDY
    t = text.strip().lower()
    if t in ("study", "s"):
        return Mode.STUDY
    if t in ("assessment", "exam", "a"):
        return Mode.ASSESSMENT if hasattr(Mode, "ASSESSMENT") else Mode.STUDY
    return Mode.STUDY


#Asks user which mode to use, defaults to study if answer is not given
def choose_mode_interactive() -> Mode:
    try:
        raw = input("Mode (study/assessment) [study]: ").strip().lower()
    except EOFError:
        raw = ""
    mode = parse_mode(raw)
    if mode == Mode.STUDY and raw not in ("", "study", "s"):
        print("Invalid mode entered. Defaulting to study mode.")
    return mode


#Prints model answer and sources from retrieved chunks
def display_response(response) -> None:
    """
    Pretty-print the model answer and the retrieved sources/chunks.
    """
    print("\n=== Answer ===")
    print(response.answer)

    print("\n=== Sources Used ===")
    chunks = getattr(response, "chunks", None)
    if not chunks:
        print("No chunks received.")
        return

    # Loop over chunks (supports dicts or objects)
    for i, chunk in enumerate(chunks, start=1):
        if isinstance(chunk, dict):
            source = chunk.get("source")
            score = chunk.get("score")
            text = chunk.get("text", "")
        else:
            source = getattr(chunk, "source", None)
            score = getattr(chunk, "score", None)
            text = getattr(chunk, "text", "")

        print(f"[{i}] {source} (score={score})")
        #Avoid dumping super long text
        preview = text if len(text) <= 700 else text[:700] + "…"
        print(preview)
        print("-" * 60)



def build_pipeline() -> Orchestrator:
    retriever = BasicRetriever()
    llm = LLM_Client()  
    return Orchestrator(retriever, llm)


#main CLI loop for testing application flow

def run_repl(k: int, json_out: bool) -> None:
    mode = choose_mode_interactive()
    orch = build_pipeline()
    print("BIFS 614 Custom LLM Application Flow Demo")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            question = input("\nPlease enter your question: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if question.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if not question:
            print("Please enter a non-empty question.")
            continue

        try:
            response = orch.answer(question, mode=mode, k=k)
        except Exception as e:
            print(f"Error while answering: {e}", file=sys.stderr)
            continue

        if json_out:
            payload = response.dict() if hasattr(response, "dict") else response.__dict__
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            display_response(response)

#single question mode, non-interactive for Powershell scripting
def run_one_shot(question: str, mode: Mode, k: int, json_out: bool) -> int:
    orch = build_pipeline()
    try:
        response = orch.answer(question, mode=mode, k=k)
    except Exception as e:
        print(f"Error while answering: {e}", file=sys.stderr)
        return 1

    if json_out:
        payload = response.dict() if hasattr(response, "dict") else getattr(response, "__dict__", {})
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        display_response(response)
    return 0

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="CLI for the LLM application flow (Retriever -> Context -> LLM)."
    )

    parser.add_argument(
        "-k", "--topk",
        help="Top-k chunks to retrieve",
        type=int,
        default=4
    )
    parser.add_argument(
        "--json",
        help="Output JSON instead of pretty text",
        action="store_true",
    )
    parser.add_argument(
        "-q", "--question",
        help="One-shot question (non-interactive mode). If omitted, starts REPL.",
        default=None
    )

    args = parser.parse_args(argv)

    if args.question:
        # one-shot path still needs a mode
        mode = choose_mode_interactive()
        return run_one_shot(args.question, mode=mode, k=args.topk, json_out=args.json)
    else:
        # REPL path – run_repl handles mode selection
        run_repl(k=args.topk, json_out=args.json)
        return 0

if __name__ == "__main__":
    raise SystemExit(main())