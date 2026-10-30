# external imports
from typing import Protocol

# internal imports
from .capabilities.llm import LLMCapabilities
from .capabilities.tool import ToolCapabilities
from .capabilities.communication import CommunicationCapabilities
from .capabilities.memory import MemoryCapabilities


class Context(
    LLMCapabilities,
    ToolCapabilities,
    CommunicationCapabilities,
    MemoryCapabilities,
    Protocol,
):
    """
    context layer is the interface/intermediate layer
    between system (agent system) and external world.
    """

    @property  # @property here help acessing the value of session id.
    def session_id(self) -> str:  # like `context.session_id`,
        ...

    @property  # same as above
    def run_id(self) -> str: ...
