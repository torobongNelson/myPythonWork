request_prompt = input("what is your problem ?")

if request_prompt:
    request_prompt_two = input("Have you had this problem before (yes or no)?")
    if request_prompt_two == "yes":
        print("Well, you have it again")

    if request_prompt_two == "no":
        print("Well, you have it now")