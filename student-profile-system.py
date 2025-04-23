# STUDENT PROFILE SYSTEM USING COLLECTIONS IN PYTHON

# student_profile dict
student_profile = {}

while True:
    user_input = str(input(
'''
===== STUDENT PROFILE SYSTEM =======
    1. Add Profile
    2. View Profile
    3. Add Skill
    4. View Skills
    5. Update Address
    6. Delete a Field
    7. Convert to Tuple
    8. Exit
---------------------------------------------------------------------
    Enter an option to select:
'''
    )).strip()

    # Add profile
    if user_input == '1':
        #name
        student_profile['name'] = str(input("Enter your name: ")).strip().capitalize()
        #age
        while True:
            try:
                student_profile['age'] = int(input("Enter your age in numbers: "))
                break
            except:
                print("Please enter a valid number")
        #degree
        student_profile['degree'] = str(input("Enter your current degree: ")).strip().upper()
        # year
        student_profile['year'] = str(input("Enter your current year: ")).strip()
        # skills
        skills_input = input("Enter your skills by seperating them in comma: ").strip()
        skills = [skill.strip() for skill in skills_input.split(',') if skill.strip()]
        student_profile['skills'] = skills
        # address
        address = {}
        address['city'] = str(input("Enter your City: ")).strip().title()
        address['country'] = str(input("Enter your Country: ")).strip().title()
        student_profile['address'] = address

        print("\n Student profile created!")
        #loop through student profile to display
        for key, value in student_profile.items():
            print(f"{key.capitalize()} : {value}")

    # View profile
    elif user_input == '2':
        if student_profile:
            print("\n  Student Profile ")
            print("-----------------------------------")
            for key, value in student_profile.items():
                # Handle address dict
                if key == 'address' and isinstance(value, dict):
                    print("Address:")
                    for subkey, subvalue in value.items():
                        print(f"  {subkey.capitalize()} : {subvalue}")
                # Handle skills list
                elif key == 'skills' and isinstance(value, list):
                    print("Skills:")
                    for index, skill in enumerate(value, 1):
                        print(f"  {index}: {skill}")
                # Handle normal fields
                else:
                    print(f"{key.capitalize()} : {value}")
        else:
            print("No data to print.")

    # Add Skill
    elif user_input == '3':
        new_skill_input = input("Enter new skills to add seperated them by comma: ").strip()
        # convert input into string and split by comma in a list
        new_skill = [ skill.strip() for skill in new_skill_input.split(',') if skill.strip() ]
        if new_skill:
            # Convert existing skills to lowercase for case-insensitive comparison
            existing_skills = [skill.lower() for skill in student_profile['skills']]
            new_skills = []
            # Check if new skills already exist and add them to the new_skills list if they don't exist
            for skill in new_skill:
                if skill.lower() not in existing_skills:
                    new_skills.append(skill)
                else:
                    print(f"{skill} already exists and cannot be added")       
            # Add new skills to the student_profile
            if new_skills:
                student_profile['skills'].extend(new_skills)
                print("New skills were added successfully!")
            else:
                print("No skills were added!")
        else:
            print("Please enter a valid skill")

    # View Skills
    elif user_input =='4':
        if 'skills' in student_profile and isinstance(student_profile['skills'], list):
            print("\n Skills: ")
            count = 0
            for index, skill in enumerate(student_profile['skills'], 1):
                count +=1
                print(f"{index}. {skill}")
        else:
            print("Skills not found")
        print(f"\n Total Skills: {count}")


    # Update Address
    elif user_input == '5':
        if 'address' in student_profile and isinstance(student_profile['address'], dict):
            print("\n Current Address:")
            for key, value in student_profile['address'].items():
                print(f"{key.capitlize()} : {value}")

    elif user_input == '8':
        print('Thank you! Have a Nice day!')
        break

    else:
        print("Enter a valid option")
  