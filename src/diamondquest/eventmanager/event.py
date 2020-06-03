class Event:
    """
    Superclass representing any sort of event that can be managed by the EventManager
    """

    def __init__(self):
        self.name = "Generic Event"


class TickEvent(Event):
    """
    An event to tick the game state
    """

    def __init__(self):
        self.name = "Tick Event"
