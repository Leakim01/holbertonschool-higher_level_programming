#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is None:
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
