def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("UnderWeight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    elif bmi > 25.0:
        print("OverWeight")
    
    print("Your Bmi value is = " + str(bmi))


def main():
    display_main_menu()


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32):")
    user_input = get_user_input()  
    calc_average_temperature(user_input) 
    find_min_max(user_input)
    sorted_list = sort_temperature(user_input)
    calc_median_temperature(sorted_list)

def get_user_input():
    user_input = input()  
    formatted_input = user_input.split(",")
    float_list = [float(item) for item in formatted_input]
    print("Converted to float list:", float_list)
    return float_list 


def calc_average_temperature(float_list):
    total = 0  
    for i in float_list:
        total += i
    average_temp = total / len(float_list)
    print(f"The average temperature is: {average_temp}")
    

def find_min_max(float_list):
    min_max = []
    Min = min(float_list)
    min_max.append(Min)
    Max = max(float_list)
    min_max.append(Max)
    print("Minimum and maximin numbers are: " , min_max)
   
    
def sort_temperature(float_list):
    sorted_list = sorted(float_list)
    print("The list in ascending order: ", sorted_list)
    return sorted_list
    
def calc_median_temperature(float_list):

    length = len(float_list)
    mid = length // 2
    
    if length % 2 == 1:
        print("The median is: ", float_list[mid])
    else:
        print("The median is: ", (float_list[mid - 1] + float_list[mid]) / 2)



if __name__ == "__main__":
    main()
