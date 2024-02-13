# match-case is simply like Switch-Case compare to any other programming language.

str = "lnamex"

match str:
    case "name":
        print("This is name.")
    case "lname":
        print("This is not lname.")
    case _:
        print("none of above")