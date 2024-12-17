Friendly Greeting App
This is a simple Python-based GUI application built using tkinter. The app greets users, simulates an internet speed test, and generates funny nicknames for friends.

Features
Greet a Friend: Enter a friend's name, and the app will display a personalized greeting.
Internet Speed Test Simulation: Click a button to simulate an internet speed test with a loading progress bar.
Funny Nicknames: After the speed test completes, the app generates a random funny nickname for the friend.
Installation
Ensure you have Python 3.x installed on your system. You can download it from here.
Install tkinter if you don’t have it. It is usually bundled with Python. If you need to install it manually, use the following command:
On Ubuntu/Debian: sudo apt-get install python3-tk
On macOS: brew install python-tk
Usage
Clone this repository or download the script file.
Run the Python script:
bash
Copy code
python friendly_greeting_app.py
Enter a friend's name in the input box and click the "Greet" button to receive a greeting.
Click the "Test Internet Speed" button to simulate an internet speed test with a progress bar.
After the test, the app will generate a funny nickname for your friend.
Code Explanation
Greet Button: Prompts a greeting message for the entered name. If the name is empty or invalid, an error message is displayed.
Internet Speed Test Simulation: Displays a loading bar with progress, simulating the internet speed test.
Funny Nickname Generator: After the speed test, a random funny nickname is assigned to the entered name.
Dependencies
tkinter: For creating the graphical user interface.
License
This project is licensed under the MIT License - see the LICENSE file for details.

