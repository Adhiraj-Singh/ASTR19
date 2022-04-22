import math

def main():
    print("sin(x)                     x")
    for x in range(0,360,1):
        print(math.sin(math.radians(x)),end='->         ')
        print(x)
    
if __name__=="__main__":
    main()
