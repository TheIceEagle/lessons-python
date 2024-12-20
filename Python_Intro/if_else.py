# if, elif, else

age = int(input("Enter your age: "))

int

if age < 18:
    print("You are not going to army")
elif 18 <= age <= 27:
    is_student = input("""
Are you a student? 
Yes or No? 
    \n""")
    if is_student.lower() in ("yes", "yeah", "y", "да",):
        print("\nYou are not yet in army, but after some time, you will...")
    else:
        print("""\
You're in the army now
Oh, oh you're in the army - now
        """)
else:
    print("Somehow still going to army")