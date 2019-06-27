def shout():
    phrase = input("""What was that?
""")
    if phrase == phrase.upper():
        print("WHY ARE YOU SHOUTING?")
    else:
        phrase = input("""Can you speak up?
""")
        if phrase == phrase.upper():
            print("WHY ARE YOU SHOUTING?")
        else:
            phrase = input("""I still can't hear you.
""")
            if phrase == phrase.upper():
                print("WHY ARE YOU SHOUTING?")
            else:
                print("""You know what, this isn't working.
Sorry.
Bye.""")
                
response = input("""Hello! How are you?
""")
if response != response.upper():
    shout()
