class PointerNotInRangeError(Exception):
    def __init__(self, message, position):
        self.message = message
        super().__init__(message)
        self.position = position

    def __str__(self):
        return str(f"{self.message} | Caught at position {self.position}")