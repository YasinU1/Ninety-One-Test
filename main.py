# parameters - A CSV file with three columns that needs to be read (first_name, second_name, score), mix of integers and strings, no special characters

# returns - prints out to the STDOUT, a single or multiple string outlining the top scorers.


def get_top_scorers_from_file(filename):
    # Open File with name TestData.csv
    # Read the content and store it in a variable
    # Sepearate the data into thier own individual lines
    # remove the first line as its the header,
    

    # after that make a hashmap map which stores the scores as a key value pair adding the full name: score
    # Find the top scores and find the top scoring names
    # Sort alphabetically if needed and print out

    #Solution
    with open(filename, 'r') as file:
        csv_data = file.read()
        lines = csv_data.strip().split("\n")
        
        # Removes the first row so that it doesnt get read
        lines = lines[1:]
        
        # Hashmap to store all the scores
        scores_dict = {}
        
        # Split all of the lines and put full name into a key value pair
        for line in lines:
            first_name, second_name, score = line.split(",")
            full_name = f"{first_name} {second_name}"
            scores_dict[full_name] = int(score)
        
        # Find the top score
        top_score = max(scores_dict.values())
        top_scorers = [name for name, score in scores_dict.items() if score == top_score]
        
        # Sort the names alphabetically
        top_scorers.sort()
        
        # Print the result
        for scorer in top_scorers:
            print(f"{scorer}: {top_score}")

# Test the function with your CSV file
filename = "TestData.csv"
get_top_scorers_from_file(filename)

# test cases
# get_top_scorers_from_file(TestData.csv) // Sipho Lolo: 78
"""
/// get_top_scorers_from_file(
    First Name,Second Name,Score
    Dee,Moore,56
    Sipho,Lolo,78
    Noosrat,Hoosain,64
    George,Of The Jungle,78)  
    
//
George,Of The Jungle,78
Sipho Lolo: 78

"""

"""
/// get_top_scorers_from_file(
    First Name,Second Name,Score
    Dee,Moore,78
    Sipho,Lolo,78
    Noosrat,Hoosain,78
    George,Of The Jungle,78
)  
    
// STDOUT
Dee Moore: 78
George Of The Jungle: 78
Noosrat Hoosain: 78
Sipho Lolo: 78


"""
