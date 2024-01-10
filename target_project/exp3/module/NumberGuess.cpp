
// NumberGuess.cpp
#include "NumberGuess.h"
#include <iostream>  // Include the necessary header file

// Implement setAnswer function
void NumberGuess::setAnswer(int answer) {
    this->answer = answer;  // Store the answer
}

// Implement checkGuess function
bool NumberGuess::checkGuess() {
    int guess;
    std::cin >> guess;  // Get the user's guess
    return guess == this->answer;  // Check if the guess is correct
}
