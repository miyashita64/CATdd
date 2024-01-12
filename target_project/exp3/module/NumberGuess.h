#ifndef NUMBER_GUESS_H
#define NUMBER_GUESS_H

#include <iostream>

class NumberGuess{
    private:
    int answer;

    public:
    NumberGuess();
    void setAnswer(int answer);
    bool checkGuess();
};

#endif