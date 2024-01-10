
// NumberGuess.h
#ifndef NUMBERGUESS_H
#define NUMBERGUESS_H

class NumberGuess {
private:
    int answer;  // Store the answer

public:
    void setAnswer(int answer);
    bool checkGuess();
};

#endif  // NUMBERGUESS_H
