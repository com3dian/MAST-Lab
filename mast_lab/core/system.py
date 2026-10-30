"""
In this file we put the base system protocal, which will be used
to define the interface of agentic systems. To find the impleme-
tation, go to `/mast_lab/systems/` folder.

System can be agent systems, control systems, interaction systems,
monitoring or logging systems.

Agent system could be some agentic architecture design like ReAct.

Interaction system mainly for user actions like steering message.

-----------------------------
Where is this logic located within the conceptional framework?

"""

# external imports
from typing import Protocol

# internal imports
from .context import Context


# the things in []
class System[contextType, inputType, outputType](Protocol):
    async def __call__(
        self,
        context: Context,
        request: inputType,
    ) -> outputType:
        """
        Run agent system to response to user request.

        args:
            request: the input request from the user, here is the
            input type for this interface, contravariant make the
            child class to accept the parent input type, but not
            the opposite.

            context: Context

        output:
            outputType: output type for this interface, covariant
            make the child class to return the parent output type,
            but not the opposite.
        """
        ...
