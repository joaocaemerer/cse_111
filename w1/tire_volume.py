import math

def calculate_tire_volume():
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspc_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = ( math.pi * (width**2) * aspc_ratio * (width * aspc_ratio + 2540*diameter) ) / ( 10*1000*1000*1000 )
    
    print(f"The approximate volume is {volume:.2f} liters")


def main():
    calculate_tire_volume()

if __name__ == '__main__':
    main()