## import libraries
import os
import random

## read vote files
def read_votes_file():
    """Reads votes from file and store in list of dictionaries"""
    vote_list = []
    with open("votes.txt", "r") as votes_file:
        votes_data = votes_file.read().split("\n")
        votes_data = [v for v in votes_data if v != ""]
    
    for v_str in votes_data:
        curr_vote = {}
        vote_components = v_str.split(";")
        curr_vote["colour"] = vote_components[0]
        curr_vote["name"] = vote_components[1]
        curr_vote["lesson"] = vote_components[2]
        vote_list.append(curr_vote)
    return vote_list

## add vote to file
def write_votes_file(vote_list):
    """Writes votes to votes.txt file"""
    with open("votes.txt", "w") as votes_file:
        write_vote_list = []
        for v in vote_list:
            str_attrs = [
            v["colour"],
            v["name"],
            v["lesson"] 
            ]
            write_vote_list.append(";".join(str_attrs))
        votes_file.write("\n".join(write_vote_list))

def add_votes(vote_list):
    """Adds vote to vote list, then write to file using write_votes_file()"""
    vote_colour = input("Hair colour vote:\t").lower()
    vote_name = input("Enter pupil's name:\t").lower()
    vote_lesson = input("What lesson did they get the vote?\t").lower()

    new_vote ={
        "colour": vote_colour,
        "name": vote_name,
        "lesson": vote_lesson
    }
    
    vote_list.append(new_vote)
    write_votes_file(vote_list)
    print("vote added")

## view all votes
def view_all(vote_list):
    """View all votes in vote list"""

    # Divider line
    os_width = os.get_terminal_size().columns
    line = "-" * os_width
    if not vote_list:
        raise ValueError("No votes recorded.")
    print(line)
    for v in vote_list:
        disp_str = f"Name:\t{v["name"].title()}\n"
        disp_str += f"Colour:\t{v["colour"]}\n"
        disp_str += f"Class:\t{v["lesson"]}\n{line}"
        print(disp_str)

## check vote
def check_votes(vote_list):
    """Prints stats for individual"""
    vote_name = input("Who's votes would you like to check?\t").lower()
    indiv_colours = []
    votes_count = 0
    for v in vote_list:
        if vote_name == v["name"]:
            indiv_colours.append(v["colour"])
            votes_count += 1
    print(f"{vote_name.title()} has {votes_count} votes.")
    print("The votes are:")
    for c in indiv_colours:
        print(f"\t{c}")


## vote choice 
def random_generator(vote_list):
    """Selecting random vote and printing output"""
    vote_dict = random.choice(vote_list)
    disp_vote = f"The colour is...\n"
    disp_vote += f"{vote_dict["colour"].upper()}\n"
    disp_vote += f"Voted by {vote_dict["name"].title()} ({vote_dict["lesson"]})"
    print(disp_vote)


## main menu
def main_menu():
    """Menu for selection process"""
    vote_list = read_votes_file()
        # Divider line
    os_width = os.get_terminal_size().columns
    line = "-" * os_width

    while True:
        print()
        try:
            menu = int(input("""
What would you like to do?
    1 - see all votes
    2 - add vote
    3 - check person's votes
    4 - edit vote
    5 - choose hair colour
"""))
            if menu == 1:
                view_all(vote_list)
            elif menu == 2:
                add_votes(vote_list)
            elif menu == 3:
                check_votes(vote_list)
            elif menu == 4:
                print("option coming soon...")
                pass # edit vote not implemented
            elif menu == 5:
                random_generator(vote_list)
            else:
                raise ValueError(f"number not on menu.")
        except ValueError as ve:
            print(f"ERROR: {ve} Please try again.")  


if __name__ == "__main__":
    main_menu()