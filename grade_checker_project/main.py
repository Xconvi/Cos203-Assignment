
import input
import logic
import output

def main():
    # 1. Get the raw number from the input module
    grades = input.input_grade()
    
    # 2. Pass the number to the logic module to get the letter
    letter = logic.get_letter_grade(grades)
    
    # 3. Pass the letter to the outputs module to print it
    output.display_result(letter)

if __name__ == "__main__":
    main()