def main():
    # getting height and weight
    height = input('enter height(meter) : ')
    weight = input('enter weight(kg) : ')
    # parsing to its data
    try:
        height = float(height)
        weight = float(weight)
    except:
        print("invalid input !!")
        raise
    # calculating BMI
    bmi = weight / (height * height)

    # printing the BMI based result
    if bmi <= 18.5:
        print("BMI: {:.2f}".format(bmi))
        print('you are underweight.')
    elif (bmi > 18.5) and (bmi < 25):
        print("BMI: {:.2f}".format(bmi))
        print('you are normal.')
    elif (bmi > 25) and (bmi < 30):
        print("BMI: {:.2f}".format(bmi))
        print('you are overweight.')
    elif bmi > 30:
        print('you are obese.')


if __name__ == '__main__':
    main()
