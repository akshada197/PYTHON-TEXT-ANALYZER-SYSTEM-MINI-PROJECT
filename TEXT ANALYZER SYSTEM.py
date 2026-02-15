print("*************TEXT ANALYZER SYSTEM*****************")
text = input("Enter a sentence or paragraph:")
text = " ".join(text.split())

while True:
    print("----------MENU-----------")
    print("1. COUNT CHARACTERS")
    print("2. COUNT WORDS")
    print("3. COUNT SENTENCE")
    print("4. CHARACTER ANALYSIS")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE (1-5): ")
    if choice == '1':
        print("total characters : ", len(text))

    elif choice == '2':
        print("total count of words: ", len(text.split()))

    elif choice == '3':
        sentences = text.count('.') + text.count('!') + text.count('?')
        print("total count of sentences : ", sentences)  

    elif choice == '4':
        vowels = "aeiouAEIOU"
        vowels_count = consonant_count = digit_count = special_count = 0
        for ch in text:
            if ch in vowels:
                vowels_count += 1
            elif ch.isalpha():
                consonant_count += 1
            elif ch.isdigit():
                digit_count += 1
            elif not ch.isspace():
                special_count += 1

                print("VOWELS : ", vowels_count)
                print("CONSONANTS:", consonant_count)
                print("DIGITS: ", digit_count)
                print("SPECIAL CHARACTERS: ", special_count)

            elif choice == '5':
                print("Exiting Program...")
                break

           
                
            else:
                print("Invalid Choice !!")
                      





        

