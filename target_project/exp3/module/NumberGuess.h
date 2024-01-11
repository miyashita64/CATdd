#ifndef NUMBERGUESS_H
#define NUMBERGUESS_H

#include <iostream>

class NumberGuess {
public:
    void setAnswer(int answer);
    bool checkGuess();
    
private:
    int answer;
};

#endif // NUMBERGUESS_H