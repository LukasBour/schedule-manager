
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
def print_error(error: str | Exception) -> None:
    if type(error) is str:
        print(f"{BColors.FAIL}{error}{BColors.ENDC}")
    elif type(error) is Exception:
        print(f"{BColors.FAIL}{type(error).__name__}: {str(error)}{BColors.ENDC}")
    else:
        raise AttributeError(f"Attribute was {type(error)}, but str or Exception were expected.")
