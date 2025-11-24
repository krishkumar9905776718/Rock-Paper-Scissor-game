Project Documentation

Title: Rock–Paper–Scissor Game

Created by: [Krish Kumar]

1. Overview

In this project, I have built an interactive Rock–Paper–Scissor game using Python.
The program allows the user to play multiple rounds against the computer.
I used three Python modules — random, time, and os — to improve gameplay by adding randomness, timing effects, and screen clearing.
This game runs in the terminal and provides an engaging experience with round-based scoring.


2. Objective of the Project

 The main objective of this project is to:
  practice Python functions and loops
  use at least three modules
  create a simple but interactive command-line game
  apply conditional logic and user input validation
  build a complete mini-application


3. Functional Requirements

These are the things my project does:

 a. Takes user input for rock, paper, or scissor

b. Validates that the user enters a correct option


 c. lets the computer randomly choose using the random module


 d. Adds a fun countdown effect using the time module


 e. Clears the screen after every round using the os module


 f. Plays multiple rounds based on user choice


 g. Calculates and displays scores after each round

 h. declares the final winner at the end


4. Non-Functional Requirements

These describe the quality or behaviour of the project:

 a. User Friendly:
    The game gives clear instructions and handles invalid inputs smoothly.

b. Performance:
    The game responds quickly and clears the screen between rounds for a clean interface.


 c. Reliability:
    The game gives correct results because all conditions for winning/losing are properly checked.


 d. Maintainability:
    The code is organized into functions like play_round(), game(), and clear_screen(), which makes it easy to update in the future.



5. Modules Used

  a. random
     Used to generate the computer’s choice.

  b. time
     Used to add delay for countdown ("Rock Paper Scissor").

  c. os
     Used to clear the screen after each round for a smooth gameplay experience.




6. Code Explanation

 clear_screen()

   Clears the terminal screen based on whether the system is windows.

 countdown()

   Prints “Rock, Paper, Scissor” with small delays to make the game more dramatic.

 play_round()

   Takes the user input, randomly chooses computer input, compares both, returns who won the round.

 game()

   Asks for number of rounds, keeps track of scores, runs all rounds, shows the final winner.



7. Input & Output Example

Input:

Number of rounds
user move (rock/paper/scissor)


Output:

Computer’s move
winner of each round
ongoing score
final match result


8. Conclusion

Through this project, I learned how to build an interactive python game using multiple modules.
I understood how to handle user input, implement game logic, use functions, and make the interface cleaner with screen clearing and timed messages.

This project helped me practice real python programming and strengthened my understanding of loops, conditions, and modular code.

