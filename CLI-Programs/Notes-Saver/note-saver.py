# --- NOTES SAVER ---
# Write a Note
# Save it to a file
# View Saved Note
# Exit the Program

import os
from datetime import datetime

# Define file path
file_path = os.path.join('CLI-Programs', 'Notes-Saver', 'notes.txt')

# Check if the directory exists, create it if not
os.makedirs(os.path.dirname(file_path), exist_ok=True)

while True:
    try:
        response = int(input('''
            --- NOTES SAVER ------------
            Enter 1 to Write a Note.
            Enter 2 to View a Notes.
            Enter 0 to Exit the Notes.      
            ----------------------------            
        '''))
        match response:
            case 1:
                # Write Note
                try:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    user_notes: str = input("Enter your notes... ").strip()
                    if user_notes:
                        with open(file_path, 'a') as file:
                            file.write(f"[{timestamp}]: {user_notes}\n")
                        print("Notes Saved Successfully!")
                    else:
                        print("Empty Notes cannot be saved\n")
                except Exception as e:
                    print(f"[ERROR] Failed to save. {e}\n")
            case 2:
                # View Notes
                if not os.path.exists(file_path):
                    print('[INFO] No notes available yet\n')
                else:
                    try:
                        with open(file_path, 'r') as file:
                            content = file.readlines()
                            if content:
                                for line in content:
                                    print(line.strip())
                            else:
                                print('[INFO] Notes file is Empty!\n')
                    except FileNotFoundError as e:
                        print(f"[ERROR] {e}")
            case 0:
                print("Exiting the program.")
                break
            case _:
                print("[ERROR] Invalid option. Please try again.")
    except ValueError:
        print('[ERROR] Please Enter a Valid Input')