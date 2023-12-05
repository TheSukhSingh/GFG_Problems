def isPalin(s):
    s = s.lower()
    return s == s[::-1]