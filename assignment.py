import random
def  check_age_21(age: int) -> bool:
    """
    Implement a function that checks if a given age is 21 or older
    return True if the age is 21 or older, otherwise return False

    """
    if age >= 21:
        return True
    else:
        return False





def check_grade_level(grade: str) -> bool:
    """
    Implement a function that checks if a given grade level is valid
    return True if the grade level is valid (between 9 and 12), otherwise return False
    and it must print the grade level like freshman, sophomore, junior, senior if it is valid
    """
    
    grade = int(grade)
    if grade == 9:
        return(True)
    elif grade == 10:
        return(True)
    elif grade == 11:
        return(True)
    elif grade == 12:
        return(True)
    else: 
        return(False)
    
check_grade_level(9)


    


def check_date_of_birth(date_of_birth: str) -> bool:
    """
    Implement a function that checks if a given date of birth is valid
    return True if the date of birth is valid (between 1900 and current year), otherwise return False
    and it must return the current year if it is valid
    """
    date_of_birth = int(date_of_birth)
    if date_of_birth >= 1900:
        return True
    else:
        return False




def ckeck_the_list_of_cars(car_list: list) -> bool:
    """
    Implement a function that checks if a given list of cars contains at least 3 cars
    return True if the list contains at least 3 cars with different model, otherwise return False
    and it must return the number of cars with different model if it is valid
    """
    car_list = set(car_list)
    car_list = list(car_list)

    if len(car_list) >= 3:
        return True
    else:
        return False    




def check_if_you_can_drive(can_you_drive: str) -> bool:
    """
    Implement a function that checks if a given string can_you_drive is valid
    return True if the string can_you_drive is valid (either 'yes' or 'no'), otherwise return False
    and it must return 'You can drive' if it is valid
    """
    if can_you_drive == "yes" or can_you_drive == "no":
        return True
    else:
        return False





def check_weather(weather: str) -> bool:
    """
    Implement a function that checks if a given weather is valid
    create a list of valid weather conditions ['sunny', 'rainy','snowy', 'wind'] 
    and check if the weather is in the list if true return True otherwise return False
    and it must return the weather if it is valid
    """

    validweather=['sunny', 'rainy','snowy', 'wind']
    if weather in validweather:
        return True 
    else:
        return False

def check_if_you_can_play_game(can_you_play_game: str) -> str:
    """
    Check if a given string can_you_play_game is valid and randomly return
    'You can play game' if valid, otherwise return False.
    """
    # Check if the input is valid (non-empty in this case)
    if can_you_play_game:
        # Generate a random boolean
        can_play = random.choice([True, False])
        if can_play:
            return 'You can play game'
    return False




def check_study_time_or_play_time(study_time_or_play_time: str) -> bool:
    """
    Implement a function that checks if a given study_time_or_play_time is valid
    create a list of valid study_time_or_play_time ['study', 'play']
    and check if the study_time_or_play_time is in the list if true return True otherwise return False
    and it must return the study_time_or_play_time if it is valid
    """

    if study_time_or_play_time in (['study', 'play']):
            return True
    else:
        return False



def make_the_input_store_in_variable(input_string: str) -> str:
    """
    Implement a function that takes a string input_string and stores it in a variable named 'user_input'
    return the user_input string
    and use if-else statements to check the type of the input_string and convert it to the appropriate data type
    """

    user_input = input_string
    try:
        user_input = float(user_input)

        if user_input == int(user_input):
            return int(user_input)
        else:
            return user_input
    except:
        return user_input


def check_if_the_number_is_even(number: int) -> bool:
    """
    Implement a function that checks if a given number is even
    return True if the number is even, otherwise return False
    """
    x = number
    if (x%2):
        return False
    else:
        return True
