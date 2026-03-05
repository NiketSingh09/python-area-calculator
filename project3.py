def area(shape):
    if(shape == "triangle"):
        height = int(input("enter the height of your triangle : "))
        base = int(input("enter the base of your triangle : "))
        print("area of your triangle is ; " , 0.5*height*base)
    elif(shape == "circle"):
        radius = int(input("enter the radius of your circle : "))
        print("area of your circle is " , 3.14*radius*radius)
    elif(shape == "square"):
        length = int(input("enter the lenght of your square : "))
        print("area of your square is : " , length*length)
    elif(shape == "rectangle"):
        length = int(input("enter the length of your rectangle : "))
        b = int(input("enter the breath of your rectangle : "))
        print("area of your rectangle is : ", length*b)
    else:
        print("not a valid shape")

while True:
    s = input("enter the shape whose area you want : ").lower()
    area(s)
    choice = input(" do you still want to continue ? : (y/n) ")
    if (choice == "n"):
        break
