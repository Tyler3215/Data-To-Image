from PIL import Image

class Encoder:
    def __DataToHex(self, data: str) -> str:
        return ''.join(hex(ord(char))[2:] for char in data)

    def __DataToColors(self, dataHex: str) -> list[int]:
        hashmap = {"0":0, "1":16, "2":32, "3":48,
                "4":64, "5":80, "6":96, "7":112,
                "8":128, "9":144, "a":160, "b":176,
                "c":192, "d":208, "e":224, "f":240}
        
        return [hashmap[char] for char in dataHex]
        
    def __ColorsToVideo(self, dataColors: list[int], lastIndex: int) -> int:
        image = Image.new("RGB", (25, 25))
        X, Y = image.size
        x,y = 0,0

        for index in range(lastIndex, len(dataColors)):
            if x == X:
                y+=1
                x=0
            image.putpixel((x,y), (dataColors[index], dataColors[index], dataColors[index])) #pixels[x,y] = (colors[index], colors[index], colors[index])
            
            #print(x,y)
            if y == Y-1 and x == X-1:
                print("We need new foto!!!")
                image.save("obraz.tiff")
                return index # retrun last index. We need that to know where we ended
            x+=1

        image.save("obraz.tiff")
        return 0
    
Encoder("Hej ziomo")