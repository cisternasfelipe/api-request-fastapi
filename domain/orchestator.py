from __future__ import annotations
from agent import Agent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from planner import Planner

class Orchestator(Agent):
    