

def output(grade):
    print(logic(grade))

def logic(grade):

    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"  # Anything below 60 is considered failing

def input_grade():
    grade = float(input("Enter the grade: "))
    return grade

def main():
    grade = input_grade()
    output(grade)

# Standard Python boilerplate: ensures main() is only called if this script 
# is run directly (not if it's imported as a module into another script).
if __name__ == "__main__":
    main()