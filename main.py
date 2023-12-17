from PIL import Image
import os
class Encoder:
    def __init__(self, data: str) -> None:
        dataColors = self.__HexToColors(dataHex=self.__DataToHex(dataString=data))
        lastIndex = 0
        for i in range(self.__HowManyImages(data=data)):
            lastIndex = self.__ColorsToImages(dataColors=dataColors, lastIndex=lastIndex, lap=i)

    def __DataToHex(self, dataString: str) -> str:
        return bytes(dataString, 'ascii').hex() #return ''.join(hex(ord(char))[2:] for char in dataString)

    def __HexToColors(self, dataHex: str) -> list[int]:
        hashmap = {"0":0, "1":16, "2":32, "3":48,
                "4":64, "5":80, "6":96, "7":112,
                "8":128, "9":144, "a":160, "b":176,
                "c":192, "d":208, "e":224, "f":240}
        return list(hashmap[char] for char in dataHex)

    def __HowManyImages(self, data: str) -> int:
        lenghtOfDataTimes2 = len(data) * 2
        sizeOfFrame = 256
        if lenghtOfDataTimes2 > sizeOfFrame: return lenghtOfDataTimes2 // sizeOfFrame if lenghtOfDataTimes2 % sizeOfFrame == 0 else (lenghtOfDataTimes2 // sizeOfFrame) + 1
        return 1

    def __ColorsToImages(self, dataColors: list[int], lastIndex: int, lap: int) -> int:
        image = Image.new("RGB", (16, 16))
        X, Y = image.size
        x,y = 0,0
        for index in range(lastIndex, len(dataColors)):
            if x == X:
                y+=1
                x=0
            image.putpixel((x,y), (dataColors[index], dataColors[index], dataColors[index])) #pixels[x,y] = (colors[index], colors[index], colors[index])
            if y == Y-1 and x == X-1:
                image.save(f"image{lap}.tiff")
                return index # retrun last index. We need that to know where we ended
            x+=1
        image.save(f"image{lap}.tiff")
        return 0
    
def NumbersOnly(func: any):
    def wrapper(self, images: str):
        if not images.isdigit():
            raise TypeError("Only numbers can be inserted. Try again")
        return func(self, images)
    return wrapper
class Decoder:
    def __init__(self) -> None:
        self.__decodedString = self.__HexToData(self.__ColorsToHex(self.__PixelsToColors(self.__GetPath(input("How many images do you want to decode? ")))))

    @NumbersOnly
    def __GetPath(self, images: str) -> list[str]:
        print(f"Your corrent dir is: {os.getcwd()}")
        paths = list()
        for i in range(1, int(images)+1):
            while True:
                path = input(f"Path to image {i}: ")
                if os.path.exists(path) and path[-5:] == ".tiff":
                    paths.append(path)
                    break
                else:
                    print("That path doesn't exists or file type isn't .tiff")
        return paths if len(paths) == int(images) else 0
    
    def __PixelsToColors(self, paths: list[str]) -> list[int]:
        colors = list()
        for path in paths:
            image = Image.open(path)
            colors += list(image.getdata())
        return list(color[0] for color in colors)
    
    def __ColorsToHex(self, dataColors: list[int]) -> list[str]:
        hashmap = {0:"0", 16:"1", 32:"2", 48:"3",
                64:"4", 80:"5", 96:"6", 112:"7",
                128:"8", 144:"9", 160:"a", 176:"b",
                192:"c", 208:"d", 224:"e", 240:"f"}
        
        return list(hashmap[dataColors[i]]+hashmap[dataColors[i+1]] for i in range(0, len(dataColors),2))
    
    def __HexToData(self, dataHex: list[str]) -> str:
        return str(bytes.fromhex("".join(hex for hex in dataHex)).decode('ascii'))
        
    def GetDecodedString(self) -> str:
        return self.__decodedString
