# Determine the user's life stage based on their age
def generate_profile(age: int) -> str:
    if 0 < age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

if __name__ == "__main__":
    # Get User Input
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    
    # Calculate current age
    current_age = 2025 - birth_year
    
    # Generate life stage
    life_stage = generate_profile(current_age)
    
    # Gather hobbies
    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby != "stop":
            hobbies.append(hobby)
        else:
            break
    
    # Create user profile dictionary
    user_profile = {
        "name": user_name,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies
    }
    
    # Display the output
    print("\nProfile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life stage: {user_profile['stage']}")
    
    if user_profile['hobbies']:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")
    else:
        print("You didn't mention any hobbies.")