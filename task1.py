from shapely.geometry import Point


def input_cd():
    try:
        input_e = float(input("Input British National Grid coordinate ""\n""Easting:"))
        input_n = float(input("Northing:"))
        pt = Point(input_e, input_n)
        if 430000 <= input_e <= 465000 and 80000 <= input_n <= 95000:
            return pt
        else:
            print("The input location is out of range!")
            raise SystemExit
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        return input_cd()


