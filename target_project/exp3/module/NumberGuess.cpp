
#include "NumberGuess.h" // Include the header file
#include <iostream> // Include iostream for cin and cout

void NumberGuess::setAnswer(int answer) {
    this->answer = answer; // Set the answer
}

bool NumberGuess::checkGuess() {
    int guess;
    std::cin >> guess; // Take user input for guess
    return guess == answer; // Check if the guess is correct
}
