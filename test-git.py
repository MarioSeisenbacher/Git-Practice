print("Hello World")

name_01 = "Alexander Schuster"
name_02 = "Mario Zeller"
name_03 = "Jakob Lonauer"
MaMA_MIOA = []
MaMA_MIOA.append(name_01)
MaMA_MIOA.append(name_02)
MaMA_MIOA.append(name_03)

def xyz(name: str) -> str:
    name = name.split(" ")

    print(name)
    return name

 
## Für jeden Namen soll die Funktion ausgeführt werden

for name in MaMA_MIOA:
    try:
        xyz(name)
    except:
        print("Something didn't work out as expected")    
