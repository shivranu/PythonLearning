def get_greeting(day):
    match day:
        case "Monday":
            return "Hello, hope you had a great weekend!"
        case "Tuesday" | "Wednesday" | "Thursday":
            return "Hello, have a productive day!"
        case "Friday":
            return "Hello, the weekend is almost here!"
        case "Saturday" | "Sunday":
            return "Hello, enjoy your weekend!"
        case _:
            return "Hello, have a nice day!"

print(get_greeting("Monday"))     # Output: Hello, hope you had a great weekend!
print(get_greeting("Wednesday"))  # Output: Hello, have a productive day!
print(get_greeting("Friday"))     # Output: Hello, the weekend is almost here!
print(get_greeting("Sunday"))     # Output: Hello, enjoy your weekend!
print(get_greeting("Holiday"))    # Output: Hello, have a nice day!