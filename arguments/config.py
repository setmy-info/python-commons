from arguments.argument import Argument


class Config:

    def __init__(self, name: str, arguments: [Argument]):
        self.name = name
        self.arguments = arguments
