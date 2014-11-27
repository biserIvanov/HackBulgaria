from cinemaDB_creation import show_movies, show_movie_projections, cancel_reservation, make_reservation


def main():
    inpt = ""
    while(inpt != "exit"):
        inpt = input("\nCommands:\n -<show_movies>\n -<show_movie_projections <movie_id> [<date>] >\n -<make_reservation>\n -<cancel_reservation <name> >\n -<exit>\n -<help>\n>>>")
        if inpt == "show_movies":
            show_movies()
        elif "show_movie_projections" in inpt:
            arguments = inpt[23:]
            if " " in arguments:
                for i in range(len(arguments)):
                    if arguments[i] == " ":
                        show_movie_projections(arguments[:i], arguments[i+1:])
            else:
                show_movie_projections(arguments)
        elif inpt == "make_reservation":
            make_reservation()
        elif inpt == "help":
            print("This is a simple cinema-reservation system. If you do not understand\n what each of the commands are doing you are probably an idiot.")
            continue
        elif "cancel_reservation" in inpt:
            cancel_reservation(inpt[19:])

if __name__ == "__main__":
    main()
