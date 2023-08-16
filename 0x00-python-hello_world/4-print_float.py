import math

# circle
def get_area(shape):
    shape = shape.lower()
    if shape == "circle":
        cicle_area()
    elif shape == "rectangle":
        rectangle_area()
    else:
        print("Enter correct shape: ")

def cicle_area():
    radius = int(input("Enter the radius: "))

#     area = pi * r ^2
    area_of_circle = math.pi * math.pow(radius, 2)

    print("{:.2f}".format(area_of_circle))

def rectangle_area():
    width = int(input("Enter the width: "))
    length = int(input("Enter the lenth: "))
    area_of_rectangle = width * length
    print("the area of the rectangle is:{} ".format(area_of_rectangle))
def main():

    get_the_shape = input("Enter: ")
    return get_area(get_the_shape)

main()

shape_name = input("Enter: ")
shape_name = shape_name.lower()

if shape_name == "circle":
    rad = float(input("Enter radius: "))
    area_circle_2 = math.pi * math.pow(rad, 2)
    print("circle area {:.2f}".format(area_circle_2))
elif shape_name == "rectangle":
    with_2 = float(input("Enter the width: "))
    lenth_2 = float(input("Enter the length: "))

    if with_2 > 0 and lenth_2 > 0:
        area_of_rectangle_2 = with_2 * lenth_2
        print("th area of the rectangle is: {:.2f}".format(area_of_rectangle_2))
    elif with_2 == 0 or lenth_2 == 0:
        print("the area of the rectangle is ", 0)
    else:
        print("incorect")
else:
    print("Enter the 'circle' or 'rectangle'")


for i in range(1,101):
