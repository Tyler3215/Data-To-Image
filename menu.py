import main
def ResolutionMenu(encoder):
    while True:
        char = input(f"{'='*74}\n Do you want to change the resolution of the image?\n Enter 'Y' to change the resolution or 'N' to keep the default (640x480).\n{'='*74}\n")
        if char.lower() == 'y': 
            encoder.SetResolution(input("Enter width: "), input("Enter height: "))
            break

        elif char.lower() == 'n': break
        else:
            print("Please enter 'Y' or 'N' only.")

def EncoderMenu(encoder):
    while True:
        char = input(f"{'='*60}\n Enter 'S' to encode a string or 'F' to encode a text file.\n{'='*60}\n")
        if char.lower() == 's': 
            encoder.EncodeString(input("Enter string which you want to encode:\n"))
            break

        elif char.lower() == 'f':
            encoder.EncodeFile(input("Enter path to file which you want to encode:\n"))
            break

        else:
            print("Please enter 'S' or 'F' only.")

def DecoderMenu(decoder):
    while True:
        char = input(f"{'='*66}\n Enter 'S' to decode to a string or 'F' to decode to a text file.\n{'='*66}\n")
        if char.lower() == 's': 
            string = decoder.DecodeToString()
            print(string)
            break

        elif char.lower() == 'f':
            decoder.DecodeToFile(input("Enter path to txt file:\n"))
            break

        else:
            print("Please enter 'S' or 'F' only.")

if __name__ == "__main__":
    while True:
        char = input(f"{'='*18} MENU {'='*18}\n Enter 'E' for encoder or 'D' for decoder\n{'='*42}\n")
        if char.lower() == 'e':
            encoder = main.Encoder() 
            ResolutionMenu(encoder)
            EncoderMenu(encoder)
            break
            
        elif char.lower() == 'd':
            decoder = main.Decoder()
            DecoderMenu(decoder)
            break

        else:
            print("Please enter 'E' or 'D' only.")

