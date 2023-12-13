import unittest
from common.difference import Difference
from common.catdd_info import CATddInfo
from common.log import Log

class TestDifference(unittest.TestCase):
    def test_difference_print(self):
        text1 = """


#include "Atm.h"

// Default constructor
Atm::Atm() {
    balance = 1500;
}

// Get the current balance
int Atm::getBalance() {
    return balance;
}

// Transfer money from the balance
void Atm::transfer(int amount) {
    balance -= amount;
}

// Deposit money into the balance
void Atm::deposit(int amount) {
    balance += amount;
}
"""
        text2 = """#include "Atm.h"

Atm::Atm() {
    balance = 1000;
}

Atm::Atm(int balance) {
    this->balance = balance;
}

int Atm::getBalance() {
    return balance;
}

void Atm::transfer(int amount) {
    if (amount >= 0 && amount <= balance) {
        balance -= amount;
    }
}

void Atm::deposit(int amount) {
    if (amount > 0) {
        balance += amount;
    }
}
"""
        diff = Difference(text1.split("\n"), text2.split("\n"))
        diff.line_nums()
        Log.output_path = CATddInfo.path("output/test_difference_print.log")

        for tag, before_start, before_end, after_start, after_end in diff.opcodes:        
            Log.log(f"{tag} {before_start}, {before_end}, {after_start}, {after_end}")
            Log.success(diff.before_text[before_start:before_end])
            Log.info(diff.after_text[after_start:after_end])        
        Log.save()
