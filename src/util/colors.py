# Jackson Harding
# CS-172-A
# CS-172-60

# A class of ansi escape sequences
class Colors:
    def __init__(self, enabled=True):
        # Normal Colors
        self.BLACK = "\u001B[30m";
        self.RED = "\u001B[31m";
        self.GREEN = "\u001B[32m";
        self.YELLOW = "\u001B[33m";
        self.BLUE = "\u001B[34m";
        self.MAGENTA = "\u001B[35m";
        self.CYAN = "\u001B[36m";
        self.WHITE = "\u001B[37m";
        self.RESET = "\u001B[38m";

        # Light Colors
        self.LIGHT_BLACK = "\u001B[90m";
        self.LIGHT_RED = "\u001B[91m";
        self.LIGHT_GREEN = "\u001B[92m";
        self.LIGHT_YELLOW = "\u001B[93m";
        self.LIGHT_BLUE = "\u001B[94m";
        self.LIGHT_MAGENTA = "\u001B[95m";
        self.LIGHT_CYAN = "\u001B[96m";
        self.LIGHT_WHITE = "\u001B[97m";

        # Background Colors (Used for the health bars and shields)
        self.BACKGROUND_BLACK = "\u001B[40m";
        self.BACKGROUND_LIGHT_BLACK = "\u001B[100m";
        self.BACKGROUND_RED = "\u001B[41m";
        self.BACKGROUND_GREEN = "\u001B[42m";
        self.BACKGROUND_YELLOW = "\u001B[43m";
        self.BACKGROUND_BLUE = "\u001B[44m";
        self.BACKGROUND_MAGENTA = "\u001B[45m";
        self.BACKGROUND_CYAN = "\u001B[46m";
        self.BACKGROUND_WHITE = "\u001B[47m";
        self.BACKGROUND_RESET = "\u001B[49m";

    # This method disables all Ansii Escape sequences
    # Use this if the console does not support ANSII escape values
    def disable(self, __name__):
        # print('Disabled colors for ', __name__)
        self.BLACK = "";
        self.RED = "";
        self.GREEN = "";
        self.YELLOW = "";
        self.BLUE = "";
        self.MAGENTA = "";
        self.CYAN = "";
        self.WHITE = "";
        self.RESET = "";

        self.LIGHT_BLACK = "";
        self.LIGHT_RED = "";
        self.LIGHT_GREEN = "";
        self.LIGHT_YELLOW = "";
        self.LIGHT_BLUE = "";
        self.LIGHT_MAGENTA = "";
        self.LIGHT_CYAN = "";
        self.LIGHT_WHITE = "";

        self.BACKGROUND_BLACK = "";
        self.BACKGROUND_LIGHT_BLACK = "";
        self.BACKGROUND_RED = "";
        self.BACKGROUND_GREEN = "";
        self.BACKGROUND_YELLOW = "";
        self.BACKGROUND_BLUE = "";
        self.BACKGROUND_MAGENTA = "";
        self.BACKGROUND_CYAN = "";
        self.BACKGROUND_WHITE = "";
        self.BACKGROUND_RESET = "";
