from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from fastmcp import Client


class BaseAgent(ABC):
    name: str

    @abstractmethod
    async def run(self, client: Client) -> dict[str, Any]:
        raise NotImplementedError
