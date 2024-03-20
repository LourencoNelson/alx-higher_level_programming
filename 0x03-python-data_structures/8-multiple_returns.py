#!/usr/bin/python3

def multiple_returns(sentence):
    ch = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), ch)
