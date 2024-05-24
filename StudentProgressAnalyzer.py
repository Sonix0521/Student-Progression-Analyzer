from Histogram_ProgressionAnalyzer import *

print('\n\t' + "\033[1m STUDENT PROGRESSION OUTCOME ANALYZER \033[0m" + '\n')

# ====================================================== Function : Generating PROGRESS OUTCOME ====================================================== #

def progress_outcome ( pass_credit , defer_credit , fail_credit ) :

    total_credits = pass_credit + defer_credit + fail_credit

    if total_credits == 120 :
          
        if pass_credit == 120 and defer_credit == 0 and fail_credit == 0 :
            return ("\nProgression outcome : 'PROGRESS'\n")

        elif ( pass_credit == 100 and defer_credit == 20 and fail_credit == 0 ) or ( pass_credit == 100 and defer_credit == 0 and fail_credit == 20 ) :
            return ("\nProgression outcome : 'PROGRESS (TRAILER)'\n")

        elif ( 0 <= pass_credit <= 100 and 0 <= defer_credit <= 120 and 0 <= fail_credit <= 60 ) : 
            return ("\nProgression outcome : 'MODULE RETRIEVER'\n")

        else :
            return ("\nProgression outcome : 'EXCLUDE'\n")

    else :
          return ("\n\tTOTAL INCORRECT\n")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# ================================================= Function : PROGRAM REPITITION for Invalid input ================================================== #

def user_repition (repeat_program) :

    while True :
    
        ValidInput_for_repeat_program = [ 'Y' , 'Q' ]
        
        if repeat_program.capitalize() not in ValidInput_for_repeat_program :
            repeat_program = input("\nInvalid input. Enter 'Y' for yes or 'Q' to quit : ")
            print('\n----------------------------------------------------------\n')
            continue

        break

    return repeat_program

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# =================================================== Function : Display the LIST OF ENTERED DATA ==================================================== #

def UserData_list () :

    print('-------------------------------------\n')

    for data in user_input_data :
        progress_outcome_data = data[3].split(':')[1].strip()
        print(f"{progress_outcome_data} : {data[0]} , {data[1]} , {data[2]}\n")

    print('-------------------------------------\n')

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# ================================================== Function : Display the TEXTFILE OF ENTERED DATA ================================================= #

def UserData_textfile () :
    
    with open ('SD_CourseWork_TextFile.txt','a') as UserInput_text_file :

        for data in user_input_data :
            progress_outcome_data = data[3].split(':')[1].strip()
            UserInput_text_file.write(f"{progress_outcome_data} : {data[0]} , {data[1]} , {data[2]}\n")

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #



progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

user_input_data = []

while True : 
        
    try :

        print('----------------------------------------------------------')
        print("Are you a Student or a Staff member ? ( Student / Staff )")
        user_type = input('User : ')
        print('----------------------------------------------------------\n')

        while True :

            if user_type.upper() in [ 'STUDENT' , 'STAFF' ] :

                try :

                    valid_user_inputs = [0,20,40,60,80,100,120]  

                    while True :
                        try :
                            pass_credit = int(input("Enter your total PASS credits    : "))

                            if pass_credit not in valid_user_inputs :
                                print('\n\tOUT OF RANGE\n')
                                continue      

                        except ValueError :
                            print("\n\tINVALID INPUT. Integer required.\n")

                        else :
                            break

                    while True :
                        try :
                            defer_credit = int(input("Enter your total DEFER credits   : "))
                            
                            if  defer_credit not in valid_user_inputs :
                                print('\n\tOUT OF RANGE\n')
                                continue

                        except ValueError :
                            print("\n\tINVALID INPUT. Integer required.\n")

                        else :
                            break

                    while True :
                        try :
                            fail_credit = int(input("Enter your total FAIL credits    : "))

                            if fail_credit not in valid_user_inputs :
                                print('\n\tOUT OF RANGE\n')
                                continue

                        except ValueError :
                            print("\n\tINVALID INPUT. Integer required.\n")

                        else :
                            break

                except KeyboardInterrupt :
                    print("\n ======================= Program TERMINATED : KeyboardInterrupt ======================= \n")
                    exit()


                # Excute Function : Display the progress outcome
                progress_outcome_variable = progress_outcome ( pass_credit , defer_credit , fail_credit )
                print(progress_outcome_variable)


                if user_type.upper() == 'STUDENT' :

                    if progress_outcome_variable == "\n\tTOTAL INCORRECT\n" :
                        continue

                    else :
                        exit()

                elif user_type.upper() == 'STAFF' :

                    if progress_outcome_variable == "\nProgression outcome : 'PROGRESS'\n" :
                        progress_count += 1
                        
                    elif progress_outcome_variable == "\nProgression outcome : 'PROGRESS (TRAILER)'\n" :
                        trailer_count += 1
                        
                    elif progress_outcome_variable == "\nProgression outcome : 'MODULE RETRIEVER'\n" :
                        retriever_count += 1
                        
                    elif progress_outcome_variable == "\nProgression outcome : 'EXCLUDE'\n" : 
                        exclude_count += 1

                    else :
                        if progress_outcome_variable == "\n\tTOTAL INCORRECT\n" :
                            continue


                    # Data List : Saving user entered data & Progression outcome into a list
                    user_input_data.append ( [ pass_credit, defer_credit, fail_credit, progress_outcome_variable ] )

                    print('----------------------------------------------------------')

                    print('Would you like to enter another set of data?\n')

                    repeat_program = input("Enter 'Y' for yes or 'Q' to quit and view results : ")
                    
                    print('----------------------------------------------------------\n')

                    
                    # Excute function : Repition of the program by user preference
                    repitition_variable = user_repition (repeat_program)

                    if repitition_variable.capitalize() == 'Y' :
                        continue
                    
                    elif repitition_variable.capitalize() == 'Q' :

                        try :
                            # Excute function : Histogram for user entered data
                            graph_for_histogram ( progress_count , trailer_count , retriever_count , exclude_count )

                        except GraphicsError :
                            print("\n\tWindow Closed by user.\n")

                        # Excute function : List of the users entered progression data 
                        UserData_list()

                        # Excute function : Textfile of the users entered progression data 
                        UserData_textfile()

                        exit()

            else :
                print('\tINVALID USER TYPE\n')
                break

            
    except KeyboardInterrupt :
        print('\n ======================= Program TERMINATED : KeyboardInterrupt ======================= \n')

        break
