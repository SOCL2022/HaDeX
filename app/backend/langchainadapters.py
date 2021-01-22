from typing import Any, Dict, List, Optional
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult

def ch(text: str) -> str:
    s = text if isinstance(text, str) else str(text)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace("\r", "").replace("\n", "<br>")

class HtmlCallbackHandler (B