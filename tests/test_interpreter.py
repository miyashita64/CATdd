import unittest
from unittest import mock
from common.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    @mock.patch("builtins.input", return_value="y")
    def test_yn_y(self, mock_input):
        is_yes = Interpreter.yn("please input")
        assert is_yes

    @mock.patch("builtins.input", return_value="yes")
    def test_yn_yes(self, mock_input):
        is_yes = Interpreter.yn("please input")
        assert is_yes

    @mock.patch("builtins.input", return_value="n")
    def test_yn_n(self, mock_input):
        is_yes = Interpreter.yn("please input")
        assert not is_yes

    @mock.patch("builtins.input", return_value="no")
    def test_yn_no(self, mock_input):
        is_yes = Interpreter.yn("please input")
        assert not is_yes

    @mock.patch("builtins.input", return_value="yahoo")
    def test_yn_yahoo(self, mock_input):
        is_yes = Interpreter.yn("please input")
        assert not is_yes

    @mock.patch("builtins.input", return_value="other")
    def test_yn_other(self, mock_input):
        is_yes = Interpreter.yn("please input")
        assert not is_yes
