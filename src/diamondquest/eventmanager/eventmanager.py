class EventManager:
    """this object is responsible for coordinating most communication
    between the Model, View, and Controller.
    http://ezide.com/games/writing-games.html
    """

    def __init__(self):
        from weakref import WeakKeyDictionary

        self.listeners = WeakKeyDictionary()

    # ----------------------------------------------------------------------
    def register_listener(self, listener):
        self.listeners[listener] = 1

    # ----------------------------------------------------------------------
    def unregister_listener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    # ----------------------------------------------------------------------
    def post(self, event):
        """Post a new event.  It will be broadcast to all listeners"""
        for listener in self.listeners.keys():
            # NOTE: If the weakref has died, it will be
            # automatically removed, so we don't have
            # to worry about it.
            listener.Notify(event)
