def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 24.9:
        return "Normal weight"
    if bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print('Please enter valid numbers for weight and height.')
        return None, None
    
def main():
    weight, height = get_user_input()
    if weight is None or height is None:
        return
        
    try:
        bmi = calculate_bmi(weight, height)
        category = bmi_category
        print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()