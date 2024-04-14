
n = int(input("Enter the input number : "))

match n: 

    case 0:
        print("n is zero")
    
    case 4:
        print("case is 4")

    case _ if n!=80:
        print(n, "is not 80")

    case _ if n!=90:
        print(n, "is not 90")

    case _ :
        print(n)
     