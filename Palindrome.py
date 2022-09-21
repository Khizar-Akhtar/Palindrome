

while 1:
    import re
    a=input("Please enter a string to check for Palindrome or 'exit' to quit :")
    b= re.sub(pattern="\W",repl="",string=a)
    x=b.lower()

    y=x[::-1]
    if x=="exit":
      exit(0)

    elif x==y:
      print("Input is Palindrome")
    elif x != y:
     print("Input is not a Palindrome")