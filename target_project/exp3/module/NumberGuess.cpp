#include "NumberGuess.h"

NumberGuess::NumberGuess() {
    answer = 0;
}

void NumberGuess::setAnswer(int newAnswer)
{
    answer = newAnswer;
}

bool NumberGuess::checkGuess()
{
    int usersAnswer;
    std::cin >> usersAnswer;
    return (answer == usersAnswer);
}