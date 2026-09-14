from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CodingActionType(str, Enum):
    LIST_FILES = "list_files"
    READ_FILE = "read_file"
    PREVIEW_WRITE = "preview_write"
    WRITE_FILE = "write_file"


@dataclass(frozen=True)
class CodingAction:
    type: CodingActionType
    path: str = "."
    content: str | None = None
