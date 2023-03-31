Given a positive integer n, return first n dgits of Thue-Morse sequence, as a string (see examples).

Thue-Morse sequence is a binary sequence with 0 as the first element. The rest of the sequece is obtained by adding the Boolean (binary) complement of a group obtained so far.

```python
For example:

0
01
0110
01101001
and so on...
```

Ex.:

```python
thue_morse(1); #"0"
thue_morse(2); #"01"
thue_morse(5); #"01101"
thue_morse(10): #"0110100110"
You don't need to test if n is valid - it will always be a positive integer.
n will be between 1 and 10000
Thue-Morse on Wikipedia
```

https://www.codewars.com/kata/591aa1752afcb02fa300002a
