# parameters - A CSV file with three columns that needs to be read (first_name, second_name, score), mix of integers and strings, no special characters

# returns - prints out to the STDOUT, a single or multiple string outlining the top scorers.


def get_top_scorers_from_file():
    # Open File with name TestData.csv
    # Read the content and store it in a variable
    # Sepearate the data into thier own individual lines
    # remove the first line as its the header,
    

    # after that make a hashmap map which stores the scores as a key value pair adding the full name: score
    # Find the top scores and find the top scoring names
    # Sort alphabetically if needed and print out
    print("hi")

get_top_scorers_from_file()

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
