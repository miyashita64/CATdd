#include "NumberGuess.h"


NumberGuess::NumberGuess() : userInputValue(0),answer(7)
{
}

void NumberGuess::setAnswer(int _answer){
    answer = _answer;
}

bool NumberGuess::checkGuess(){
    std::string userInputValue;
    std::cin >> userInputValue;
    imputNum = stoi(userInputValue);
    if(answer == imputNum){
        return true;
    }else{
        return false;
    }
}