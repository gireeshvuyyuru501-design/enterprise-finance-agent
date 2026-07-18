from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "finance_data.json"


def load_finance_data() -> dict[str, Any]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Finance data file not found: {DATA_FILE}")

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)
