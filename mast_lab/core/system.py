"""
In this file we put the base system protocal, which will be used
to define the interface of agentic systems. To find the impleme-
tation, go to `/mast_lab/systems/` folder.

"""

# external imports
from typing import Protocol

# internal imports
from .context import Context


class System[inputType, outputType](Protocol):
    async def __call__(
        self,
        context: Context,
        request: inputType,
    ) -> outputType:
        """
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
