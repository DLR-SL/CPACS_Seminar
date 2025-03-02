from typing import Dict, Any


class MyDummyTool:
    def __init__(self, tool_data: Dict[str, Any]) -> None:

        self.tool_data = tool_data.copy()

    def run(self) -> None:
        pass

    def get_data(self) -> Dict[str, Any]:
        """Return the updated tool_data with computed results."""
        return self.tool_data
