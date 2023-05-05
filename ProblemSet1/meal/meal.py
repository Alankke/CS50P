def main():
    user_input = input("What time is it?: ").strip()
    time = convert(user_input)
    if time >= 7 and time <= 8:
        print("Breakfast time")
    elif time >= 12 and time <= 13:
        print("Lunch time")
    elif time >= 18 and time <= 19:
        print("Dinner time")
    else:
        print("")



def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + (float(minutes) /60)
    return time



if __name__ == "__main__":
    main()