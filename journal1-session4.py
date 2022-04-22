class Wolf:
    def __init__(self, lengtharms=18.2,lengthlegs=20.1,numeyes=2,tail=True,furry=True):
        self.lengtharms= lengtharms
        self.lengthlegs= lengthlegs
        self.numeyes = 2 
        self.tail = True
        self.furry = True

    def printDetails(self):
        print("A wolf has arms of length:")
        print(self.lengtharms)
        print("A wolf has legs of length:")
        print(self.lengthlegs)
        print("The wolf has ", end='')
        print(self.numeyes,end='')
        print(" eyes")
        print("The wolf has a tail")
        print("The wolf is furry")
def main():
   myfavanimal= Wolf()
   myfavanimal.printDetails()
    
if __name__=="__main__":
    main()
