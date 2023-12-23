import main
def ResolutionMenu(encoder):
    while True:
        char = input(f"{'='*73}\n Do you want to change resoltuion of image? (default 640x480) 'Y' or 'N'\n")
        if char == 'Y' or char == 'y': 
            encoder.SetResolution(input("Enter width: "), input("Enter height: "))
            break

        elif char == 'N' or char == 'n': break
        else:
            print("'Y' or 'N' only")

def EncoderMenu(encoder):
    while True:
        char = input(f"{'='*51}\n 'S' for encoding string 'F' for encoding txt file\n")
        if char == 's' or char == 'S': 
            encoder.EncodeString(input("Enter string which you want to encode:\n"))
            break

        elif char == 'd' or char == 'D':
            encoder.EncodeFile(input("Enter path to file which you want to encode:\n"))
            break

        else:
            print("'S' or 'F' only")

def DecoderMenu(decoder):
    while True:
        char = input(f"{'='*57}\n 'S' for decoding to string 'F' for decoding to txt file\n")
        if char == 's' or char == 'S': 
            string = decoder.DecodeToString()
            print(string)
            break

        elif char == 'f' or char == 'F':
            decoder.DecodeToFile(input("Enter path to txt file:\n"))
            break

        else:
            print("'S' or 'F' only")

if __name__ == "__main__":
    while True:
        char = input(f"{'='*15} MENU {'='*15}\n 'E' for encoder or 'D' for decoder\n")
        if char == 'e' or char == 'E':
            encoder = main.Encoder() 
            ResolutionMenu(encoder)
            EncoderMenu(encoder)
            break
            
        elif char == 'd' or char == 'D':
            decoder = main.Decoder()
            DecoderMenu(decoder)
            break

        else:
            print("'E' or 'D' only")

