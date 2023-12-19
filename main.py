from PIL import Image
import os

def NumbersOnly(func): #Decorator to ensure that only numbers are used as arguments.
    def wrapper(self, *args):
        for arg in args:
            if not arg.isdigit():
                raise TypeError("Only numbers can be inserted. Try again")
        return func(self, *args)
    return wrapper
class Encoder():
    def __init__(self) -> None:
        self.__width, self.__height = "640", "480" #Default image resolution.

    def __DataToHex(self, dataString: str) -> str: #Method to convert data string to hexadecimal.
        return bytes(dataString, 'ascii').hex() 
    
    def __HexToColors(self, dataHex: str) -> list[int]: #Method to convert hexadecimal data to color values.
        hashmap = {"0":0, "1":16, "2":32, "3":48,
                "4":64, "5":80, "6":96, "7":112,
                "8":128, "9":144, "a":160, "b":176,
                "c":192, "d":208, "e":224, "f":240}
        return list(hashmap[char] for char in dataHex)

    def __HowManyImages(self, lenghtOfdata: int) -> int: #Calculates the number of images needed for encoding.
        lenghtOfDataTimes2 = lenghtOfdata * 2
        sizeOfFrame = int(self.__width) * int(self.__height)
        if lenghtOfDataTimes2 > sizeOfFrame: return lenghtOfDataTimes2 // sizeOfFrame if lenghtOfDataTimes2 % sizeOfFrame == 0 else (lenghtOfDataTimes2 // sizeOfFrame) + 1
        return 1

    def __ColorsToImages(self, dataColors: list[int], lastIndex: int, lap: int) -> int: #Converts color values to images.
        image = Image.new("RGB", (int(self.__width), int(self.__height)))
        X, Y = image.size
        x,y = 0,0
        for index in range(lastIndex, len(dataColors)):
            if x == X:
                y+=1
                x=0
            image.putpixel((x,y), (dataColors[index], dataColors[index], dataColors[index]))
            if y == Y-1 and x == X-1:
                image.save(f"image{lap}.tiff")
                return index #Returns last index. We need that to know where we ended.
            x+=1
        image.save(f"image{lap}.tiff")
        return 0
    
    def __CheckPath(self, path: str) -> str: #Validates and gets the path to a text file.
        while True:
            if not os.path.exists(path) or path[-4:] != ".txt": 
                print(f"Your corrent dir is: {os.getcwd()}\n That path doesn't exists or file type isn't .txt")
                path = input("Enter new path to txt file: ")
            else: break
        return path
    
    def __ReadFile(self, path: str) -> str: #Reads data from a text file.
        with open(path, "r") as file:
            return "".join(line for line in file)
        
    def EncodeFile(self, path: str) -> None: #Encodes data from a text file.
        self.EncodeString(self.__ReadFile(self.__CheckPath(path)))

    def EncodeString(self, dataString: str) -> None: #Encodes a given string.
        dataColors = self.__HexToColors(dataHex=self.__DataToHex(dataString=dataString))
        lastIndex = 0
        for i in range(self.__HowManyImages(lenghtOfdata=len(dataString))):
            lastIndex = self.__ColorsToImages(dataColors=dataColors, lastIndex=lastIndex, lap=i)
    
    @NumbersOnly
    def SetResoultion(self, width: str, height: str) -> None: #Sets image resolution.
        if int(width) * int(height) % 2 != 0:
            raise ValueError(f"The resolution must be divisible by 2. {int(width) * int(height)} is not divisible by 2")
        self.__width, self.__height = width, height
        
class Decoder:
    @NumbersOnly
    def __GetPaths(self, images: str) -> list[str]: #Gets paths to images for decoding.
        print(f"Your corrent dir is: {os.getcwd()}")
        paths = list()
        for i in range(1, int(images)+1):
            while True:
                path = input(f"Path to image {i}: ")
                if os.path.exists(path) and path[-5:] == ".tiff":
                    paths.append(path)
                    break
                else: print("That path doesn't exists or file type isn't .tiff")
        return paths if len(paths) == int(images) else 0
    
    def __PixelsToColors(self, paths: list[str]) -> list[int]: #Converts pixel data to color values.
        colors = list()
        for path in paths:
            image = Image.open(path)
            colors += list(image.getdata())
        return list(color[0] for color in colors)
    
    def __RemovesBlanks(self, dataColors: list[int]) -> list[str]: #Removes blank values from color data.
        for i in range(0, len(dataColors),2):
            if dataColors[i] == 0 and dataColors[i+1] == 0:
                del dataColors[i:]
                break
        return dataColors
    
    def __ColorsToHex(self, dataColors: list[int]) -> list[str]: #Converts color values to hexadecimal.
        hashmap = {0:"0", 16:"1", 32:"2", 48:"3",
                64:"4", 80:"5", 96:"6", 112:"7",
                128:"8", 144:"9", 160:"a", 176:"b",
                192:"c", 208:"d", 224:"e", 240:"f"}
        
        return list(hashmap[dataColors[i]]+hashmap[dataColors[i+1]] for i in range(0, len(dataColors),2))
    
    def __HexToData(self, dataHex: list[str]) -> str: #Converts hexadecimal data to string.
        return str(bytes.fromhex("".join(hex for hex in dataHex)).decode('ascii'))
          
    def __CheckPath(self, path: str) -> str: #Validates and gets the path for output text file.
        while True:
            if os.path.exists(path) or path[-4:] != ".txt":
                print(f"Your corrent dir is: {os.getcwd()}\n That path already exists or isn't txt file!") 
                path = input("Enter new path to new txt file: ")
            else: break
        return path

    def DecodeToFile(self, path: str) -> None: #Decodes images and writes to a text file.
        with open(self.__CheckPath(path), "w") as file:
            file.write(self.DecodeToString())
    
    def DecodeToString(self) -> str: #Decodes images and returns as string.
        return self.__HexToData(self.__ColorsToHex(self.__RemovesBlanks(self.__PixelsToColors(self.__GetPaths(input("How many images do you want to decode: "))))))
    