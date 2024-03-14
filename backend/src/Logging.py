
# Specifies color values or formatting codes for usage in console prints
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Prints an error message to the console and colours it red
def print_error(message: str) -> None:
    print(f"{BColors.FAIL}{message}{BColors.ENDC}")
