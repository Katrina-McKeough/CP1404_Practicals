COLOURS_TO_CODES = {"AliceBlue": "#fof8ff", "CadetBlue1": "#98f5ff", "CornflowerBlue": "#6495ed",
                "DarkTurquoise": "#00ced1", "DeepSkyBlue1": "#00bfff", "DodgerBlue1": "#1e90ff", "LightBlue": "#add8e6",
                "LightCyan1": "#e0ffff", "LightSkyBlue": "#87cefa", "MidnightBlue": "#191970"}

colour = input("Please enter a colour name: ")
while not colour == "":
    if colour in COLOURS_TO_CODES:
        print("{} has the hexadecimal colour code {}".format(colour, COLOURS_TO_CODES[colour]))
    else:
        print("Invalid colour name.")
    colour = input("Please enter a colour name: ")
