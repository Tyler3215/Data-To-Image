from PIL import Image
import cv2, imageio
class Encoder:
    def __init__(self, data: str) -> None:
        dataColors = self.__DataToColors(dataHex=self.__DataToHex(dataString=data))
        x = 0
        for i in range(self.__HowManyFrames(data=data)):
            x = self.__ColorsToVideo(dataColors=dataColors, lastIndex=x, lap=i)
        self.__FramesToVideo(lap=i)

    def __DataToHex(self, dataString: str) -> str:
        return ''.join(hex(ord(char))[2:] for char in dataString)

    def __DataToColors(self, dataHex: str) -> list[int]:
        hashmap = {"0":0, "1":16, "2":32, "3":48,
                "4":64, "5":80, "6":96, "7":112,
                "8":128, "9":144, "a":160, "b":176,
                "c":192, "d":208, "e":224, "f":240}
        return [hashmap[char] for char in dataHex]
        
    def __ColorsToVideo(self, dataColors: list[int], lastIndex: int, lap: int) -> int:
        image = Image.new("RGB", (16, 16))
        X, Y = image.size
        x,y = 0,0
        for index in range(lastIndex, len(dataColors)):
            if x == X:
                y+=1
                x=0
            image.putpixel((x,y), (dataColors[index], dataColors[index], dataColors[index])) #pixels[x,y] = (colors[index], colors[index], colors[index])
            #print(x,y)
            if y == Y-1 and x == X-1:
                #print("We need new foto!!!")
                image.save(f"frame{lap}.tiff")
                return index # retrun last index. We need that to know where we ended
            x+=1

        image.save(f"frame{lap}.tiff")
        return 0
    
    def __HowManyFrames(self, data: str) -> int:
        lenghtOfDataTimes2 = len(data) * 2
        sizeOfFrame = 256
        if lenghtOfDataTimes2 > sizeOfFrame: return lenghtOfDataTimes2 // sizeOfFrame if lenghtOfDataTimes2 % sizeOfFrame == 0 else (lenghtOfDataTimes2 // sizeOfFrame) + 1
        return 1

    def __FramesToVideo(self, lap: int) -> None:  
        images = [imageio.imread(f"frame{i}.tiff") for i in range(lap+1)]
        imageio.mimsave('output_video.avi', images, fps=lap+1)
