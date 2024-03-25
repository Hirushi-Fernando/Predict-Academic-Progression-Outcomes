#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
# Student ID:20222197
# Date:19/04/2023

print("---------------------------------------PROGRESSION OUTCOME---------------------------------------")

def get_my_outcome(pass_credits, defer_credits, fail_credits):
    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif pass_credits == 80:
        if fail_credits == 40:
            return "Do not progress – module retriever"
        elif defer_credits == 20:
            return "Do not progress – module retriever"
    elif pass_credits <= 60:
        if fail_credits <= 60:
            return "Do not progress – module retriever"
        elif defer_credits in [20,40]:
            return "Do not progress – module retriever"
        elif pass_credits <= 40:
            if fail_credits in [0, 20]:
                return "Do not progress – module retriever"
            elif defer_credits >= 40:
                return "Exclude"
            else:
                return "Exclude"
            
# Print the histogram for each category
def print_histogram(outcomes):
    progression_count = outcomes.count("Progress")
    trailer_count = outcomes.count("Progress (module trailer)")
    retriever_count = outcomes.count("Do not progress – module retriever")
    exclude_count = outcomes.count("Exclude")
    total_count = len(outcomes)
    
    print()
    print("------------------------------------------------------------------------------")
    print()
    print("Histogram")
    print("Progress", progression_count, ": ", "*" * progression_count)                         #referred in www.w3schools.com Available from https://www.w3schools.com/python/python_strings.asp
    print("Trailer", trailer_count, ": ", "*" * trailer_count)                                  #referred in www.w3schools.com Available from https://www.w3schools.com/python/python_strings.asp
    print("Retriever", retriever_count, ": ", "*" * retriever_count)                            #referred in www.w3schools.com Available from https://www.w3schools.com/python/python_strings.asp
    print("Excluded", exclude_count, ": ", "*" * exclude_count)                                 #referred in www.w3schools.com Available from https://www.w3schools.com/python/python_strings.asp
    print()
    print(total_count, "outcomes in total.")
    print()
    print("------------------------------------------------------------------------------")
   
   
outcomes = []
All_data = []
repeat_while=True
print()
version = input("Enter student for student version or staff for staff version : ")

if(version.lower() == "student"):
    while(repeat_while):
   
    
        try:
            print()
            pass_credits = int(input("Please enter your credits at pass:"))
            # Check if pass credits is an integer and within the valid range
            if(pass_credits not in [0, 20, 40, 60, 80, 100, 120]):
                    print("Out of range.")
                    continue
                
            defer_credits = int(input("Please enter your credit at defer:"))
            # Check if defer credits is an integer and within the valid range
            if(defer_credits not in [0, 20, 40, 60, 80, 100, 120]):
                    print("Out of range.")
                    continue  
            fail_credits = int(input("Please enter your credit at fail:"))
            # Check if fail credits is an integer and within the valid range
            if(fail_credits not in [0, 20, 40, 60, 80, 100, 120]):
                    print("Out of range.")
                    continue
            elif (pass_credits + defer_credits + fail_credits != 120):
                print("Total incorrect.")
            else:
                outcome = get_my_outcome(pass_credits, defer_credits, fail_credits)
                outcomes.append(outcome)
                print(outcome)
            
                All_data.append((outcome, pass_credits, defer_credits, fail_credits))
                choice = input("Enter 'q' to quit and view results: ")
                if choice.lower() == "q":
                    break  
            
            
        except ValueError:
            print("Integer required")
            break






elif(version.lower() == "staff"):
    while True:
   
    
        try:
            print()
            pass_credits = int(input("Please enter your credits at pass:"))
            # Check if pass credits is an integer and within the valid range
            if(pass_credits not in [0, 20, 40, 60, 80, 100, 120]):
                    print("Out of range.")
                    continue
                
            defer_credits = int(input("Please enter your credit at defer:"))
            # Check if defer credits is an integer and within the valid range
            if(defer_credits not in [0, 20, 40, 60, 80, 100, 120]):
                    print("Out of range.")
                    continue  
            fail_credits = int(input("Please enter your credit at fail:"))
            # Check if fail credits is an integer and within the valid range
            if(fail_credits not in [0, 20, 40, 60, 80, 100, 120]):
                    print("Out of range.")
                    continue
            elif (pass_credits + defer_credits + fail_credits != 120):
                print("Total incorrect.")
            else:
                outcome = get_my_outcome(pass_credits, defer_credits, fail_credits)
                outcomes.append(outcome)
                print(outcome)
            
                All_data.append((outcome, pass_credits, defer_credits, fail_credits))
            
                choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
                if choice.lower() == "q":
                    break

            
        except ValueError:
            print("Integer required")
            continue
    

print_histogram(outcomes)
# Print All data
print("\nAll data:")
for data in All_data:
    print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")

