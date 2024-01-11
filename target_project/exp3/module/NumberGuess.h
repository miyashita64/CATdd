#ifndef NUMBER_GUESS
#define NUMBER_GUESS
#include <iostream>

class NumberGuess{
private:
    int userInputValue;
    int answer;
    int imputNum;

public:
    NumberGuess();
    void setAnswer(int _answer);
    bool checkGuess(void); 
};

#endif