def capture(greeting):
    match greeting:
        case "":
            print("Hello!")
        case name:
            print(f"Hi {name}!")
    if name == "Santa":
        print('Match')
