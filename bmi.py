def calculate_bmi(height, weight):
    print("Height = " + str(height) )
    print("Weight = " + str(weight) )
    bmi = weight/(height*height)
    if bmi < 18.5:
        print("UnderWeight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Wight")
    elif bmi > 25.0:
        print("OverWeight")
        
    print("Your Bmi value is = " + str(bmi))
    
calculate_bmi(weight=57, height=1.73)