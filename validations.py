#!/usr/bin/env python3

def validate_user(username, minlength):
    assert type(username) == str, "username must be string"
    if minlength < 1:
        raise ValueError("minlength must be atleast 1")

    if len(username) < minlength:
        return False

    if not username.isalnum():
        return False

    return True