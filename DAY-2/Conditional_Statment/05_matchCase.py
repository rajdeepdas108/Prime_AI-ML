color = input("Enter a color: ")

match color.lower():   # .lower() ----> help to make the input into small letters of whole input
    case "red":
        print("Color is red.")
    case "blue":
        print("Color is blue.")
    case "green":
        print("Color is green.")
    case _:
        print("Unknown color.")