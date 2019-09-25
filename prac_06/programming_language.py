class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance.

        name: string
        typing: string
        reflection: boolean
        year: integer
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Convert the instance to a string."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
