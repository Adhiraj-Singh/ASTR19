def f(x):
    return (x**3) + 8

def main():
    x = 9
    print("Printing out f(9)")
    print(f(x))
    print("Checking if result is larger than 27 (print YAY! if true)")
    if f(x) > 27:
        print("YAY!")
    
    

if __name__=="__main__":
    main()
