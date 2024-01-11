#include "NumberGuess.h"

void NumberGuess::setAnswer(int answer) {
    this->answer = answer;
}

bool NumberGuess::checkGuess() {
    int userGuess;
    std::cin >> userGuess;
    return userGuess == answer;
}