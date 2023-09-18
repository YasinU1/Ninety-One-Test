# parameters - A CSV file with three columns that needs to be read (first_name, second_name, score), mix of integers and strings, no special characters

# returns - prints out to the STDOUT, a single or multiple string outlining the top scorers.

    # Pseudo Code 
    # Open File with name TestData.csv
    # Read the content and store it in a variable
    # Sepearate the data into thier own individual lines
    # remove the first line as its the header,
    # after that make a hashmap map which stores the scores as a key value pair adding the full name: score
    # Find the top scores and find the top scoring names
    # Sort alphabetically if needed and print out

def read_csv_file(filename):
    """Read the content of a CSV file."""
    #Args:filename (str): The name of the CSV file.   
    #Returns:str: The content of the CSV file.

    with open(filename, 'r') as file:
        return file.read()

def parse_csv_data(csv_data):
    """Turns CSV data into a dictionary of names and scores."""
    #Args: csv_data (str): The CSV data as a string.  
    #Returns: dict: A dictionary with names as keys and scores as values.
   
    lines = csv_data.strip().split("\n")[1:]  # Skip the header
    return {f"{first_name.strip()} {second_name.strip()}": int(score) for first_name, second_name, score in (line.split(",") for line in lines)}



def get_top_scorers(scores_dict):
    """Get the top scorers from a dictionary of names and scores."""
    #Args:scores_object (dict): A dictionary with names as keys and scores as values.
    #Returns:list: A list of names with the top score.
    
    top_score = max(scores_dict.values())
    return sorted(name for name, score in scores_dict.items() if score == top_score)



def main(filename):
    """Main function to read, parse, and print top scorers from a CSV file."""
    try:
        csv_data = read_csv_file(filename)
        scores_object = parse_csv_data(csv_data)
        top_scorers = get_top_scorers(scores_object)
        
        top_score = max(scores_object.values())
        for scorer in top_scorers:
            print(f"{scorer}: {top_score}")
            
    #Error Handling
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: File '{filename}' has incorrect format.")

if __name__ == "__main__":
    # Run Programme
    main("TestData20.csv")


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
