from test import s1

for key in dir(s1):
    if key.isupper():
        v = getattr(s1, key)
        setattr(s1, key, v)

print(s1.USER)
