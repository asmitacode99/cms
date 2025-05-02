class BaseUseCase:
    """
    Base Use Case
    """

    def execute(self):
        self.is_valid()
        return self._factory()

    def _factory(self):
        raise NotImplementedError("Subclasses should implement this!")

    def is_valid(self):
        return True