from .builder import build_prompt
from .tasks import detect_task
from .version import PROMPT_VERSION
from datetime import datetime
from .result import PromptResult


class PromptEngine:
    """Prompt Engine"""
    
    def build(self,question):
        task = detect_task(question)
        prompt = build_prompt(question)
        
        return PromptResult(
            prompt = prompt,
            task = task,
            version = PROMPT_VERSION,
            timestamp = datetime.now()

        )

    