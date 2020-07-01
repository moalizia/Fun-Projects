program_run = 0
while program_run == 0:
    ####### Put program here #######
    Pos_vals = ["Yes", "Y", "y", "yes"]
    Neg_vals = ["No", "N", "n", "no"]
    continue_run = 0
    while continue_run == 0:
        run_input = input("Do you want to continue? (Type 'yes' or 'no')")
        if run_input in Pos_vals:
            program_run = 0
            continue_run = 1
        elif run_input in Neg_vals:
            program_run = 1
            continue_run = 1
        else:
            program_run = 0
            continue_run = 0
            print("Please type a valid response!")
