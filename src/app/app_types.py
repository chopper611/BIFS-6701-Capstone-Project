# src/app/types.py

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List, Optional, Union


class Mode(Enum):
    STUDY = "study"
    # If your project uses "assessment" or "exam", include it here:
    ASSESSMENT = "assessment"


# If your code or retriever returns structured chunks, you can use this.
# If it returns dicts, AppResponse.chunks can hold dicts too.
@dataclass
class Chunk:
    text: str = ""
    source: Optional[str] = None
    score: Optional[float] = None
    meta: Optional[dict[str, Any]] = None


@dataclass
class AppResponse:
    # Your display_response() uses response.answer and response.chunks
    answer: str = ""
    # Allow list of dicts OR Chunk objects
    chunks: List[Union[dict, Chunk]] = field(default_factory=list)

    # Optional convenience if you also want a flat list of sources
    sources: List[str] = field(default_factory=list)

    # Mode used to generate the response (study or assessment)
    mode: Optional[Mode] = None


