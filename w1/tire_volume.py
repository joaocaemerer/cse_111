import math
from datetime import datetime

def save_volume_calculation(width, aspc_ratio, diameter, volume,phone='-', file='./volumes.txt'):
    """
    Save the historical results of tire volume calculations to a file.

    This function appends the calculated tire volume along with the tire dimensions 
    (width, aspect ratio, and diameter) to a specified file. The default file name 
    is 'volumes.txt'. Each entry in the file will include the tire width in mm, 
    the tire aspect ratio, the tire diameter in inches, and the calculated volume 
    in liters.

    Args:
        width (int): The width of the tire in millimeters.
        aspect_ratio (int): The aspect ratio of the tire.
        diameter (int): The diameter of the tire in inches.
        volume (float): The calculated volume of the tire in liters.
        file (str, optional): The name of the file where the results will be saved. 
                              Defaults to 'volumes.txt'.

    Returns:
        None
    """
    with open(file, 'at') as file_append:
        file_append.write(f'{datetime.strftime(datetime.now(), "%Y-%m-%d")}, {width}, {aspc_ratio}, {diameter}, {volume:.2f}, {phone}\n')

def want_to_buy():
    """
    Ask the user if they want to buy the tire type inputted before.

    This function prompts the user to confirm whether they want to purchase tires with the specified dimensions.
    It ensures that the user provides a valid response ('yes' or 'no') and returns a boolean value based on the response.

    Returns:
        bool: True if the user wants to buy the tires, False otherwise.
    """
    valid_want_to_buy_anwser = False
    while not valid_want_to_buy_anwser:
        want_to_buy = input(f"\nDo you want to buy tires with those dimentions? (yes/no) ?")
        valid_want_to_buy_anwser = True if want_to_buy.lower() in ['yes', 'no'] else False
    if want_to_buy.lower() == 'yes':
        return True
    else:
        return False
    
def calculate_tire_volume():
    """
    Calculate the volume of a tire in liters based on user input for tire width, aspect ratio, and diameter.

    The function prompts the user to input the tire width in millimeters, the tire aspect ratio, and the tire diameter in inches.
    It then calculates the volume of the tire using the following formula:

    Volume = π * (Width^2) * Aspect Ratio * (Width * Aspect Ratio + Diameter/2,540) / 10^10

    Finally, the function prints the calculated volume in liters.

    Returns:
        None
    """
    
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspc_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = ( math.pi * (width**2) * aspc_ratio * (width * aspc_ratio + 2540*diameter) ) / ( 10**10 )
    
    print(f"The approximate volume is {volume:.2f} liters")
    
    phone = None
    if want_to_buy():
        phone = input('What is your phone number?')
    
    save_volume_calculation(width=width, aspc_ratio=aspc_ratio, diameter=diameter, volume=volume, phone=phone)

def main():
    calculate_tire_volume()

if __name__ == '__main__':
    main()