print(""" Select your browser:
      1 - Google Chrome
      2 - Firefox
      3 - MS Internet Explorer
      4 - Opera
      5 - Safari
      6 - Other """);

browser = int(input(""));
if browser == 1:
    print("Chrome");
elif browser == 2:
    print("Firefox");
elif browser == 3:
    print("MS IE");
elif browser == 4:
    print("Opera");
elif browser == 5:
    print("Safari");
elif browser == 6:
    print("Other");
else:
    print("Incorrect input")