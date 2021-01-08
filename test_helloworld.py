import pytest

from .helloworld import say_hello

def test_say_hello_1():
    assert say_hello(1) == 'hi'

def test_say_hello_2():
    assert say_hello(2) == 'Hello.'

def test_say_hello_3():
    assert say_hello(3) == 'Hmm?'
