def format_name (f_name, l_name):
    """Take a first and last name and 
    format it to return the title 
    case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name =l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("EdiNA", "iLYes"))

# Functions 
def format_name (f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name =l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

#fiuncitions with more than one input

def funcion_1(text):
    return text + text

def funcion_2(text):
    return text.title()

output = funcion_2(funcion_1("hello"))
print(output)

# Leap Year Challenge
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2100))  # False

