from enum import Enum


class ModeType(Enum):
    MAP = 1
    PUZZLE = 2
    JOURNAL = 3
    MENU = 4

    @staticmethod
    def render_order():
        """Guarantees the correct render order."""
        return [ModeType.MAP, ModeType.PUZZLE, ModeType.JOURNAL, ModeType.MENU]
