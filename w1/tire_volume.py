import math

def calculate_tire_volume():
    '''
    Calculate the volume of a tire in liters based on user input for tire width, aspect ratio, and diameter.

    The function prompts the user to input the tire width in millimeters, the tire aspect ratio, and the tire diameter in inches.
    It then calculates the volume of the tire using the following formula:

    Volume = π * (Width^2) * Aspect Ratio * (Width * Aspect Ratio + Diameter/2,540) / 10^10

    Finally, the function prints the calculated volume in liters.

    Returns:
        None
    
    '''    
    
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspc_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = ( math.pi * (width**2) * aspc_ratio * (width * aspc_ratio + 2540*diameter) ) / ( 10**10 )
    
    print(f"The approximate volume is {volume:.2f} liters")


def main():
    calculate_tire_volume()

if __name__ == '__main__':
    main()