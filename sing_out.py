def show_queue(queue):
    """Show the numbered queue and the available commands."""
    print()
    if len(queue) == 0:
        print("The queue is currently empty.")
    else:
        print("Current queue:")
        for i, singer in enumerate(queue):
            name, song = singer
            print(f"{i + 1}. {name} - {song}")
    print("\nOptions: add / next / top / remove / quit")


def prompt_for_singer():
    """Ask for a name and song, then return both cleaned up."""
    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()
    return name, song


def add_singer(queue):
    """Add a singer and song to the end of the queue."""
    name, song = prompt_for_singer()
    if name == "" or song == "":
        print("Please enter both a name and a song.")
        return
    queue.append((name, song))
    print(f"Added {name} to the queue.")


def next_singer(queue):
    """Remove and announce the first singer."""
    if len(queue) == 0:
        print("There is no one left to call up.")
        return
    name, song = queue.pop(0)
    print(f"Now up: {name} - {song}")


def move_to_top(queue):
    """Move the singer at the chosen position to the front."""
    if len(queue) < 2:
        print("You need at least two singers to reorder the queue.")
        return
    try:
        position = int(input("Which singer should move to the top? Enter a number: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if position < 1 or position > len(queue):
        print(f"Please enter a number from 1 to {len(queue)}.")
        return
    singer = queue.pop(position - 1)
    queue.insert(0, singer)
    name, song = singer
    print(f"Moved {name} to the top of the queue.")


def remove_singer(queue):
    """Remove the first singer whose name matches the input."""
    if len(queue) == 0:
        print("There is no one left to remove.")
        return
    name = input("Who do you want to remove? ").strip().title()
    if name == "":
        print("Please enter a name.")
        return
    for singer in queue:
        if singer[0] == name:
            queue.remove(singer)
            print(f"Removed {name} from the queue.")
            return
    print(f"There is no one named {name} in the queue.")


def run_app(queue):
    """Keep showing the queue and handling commands until quit."""
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)
    is_running = True
    while is_running:
        show_queue(queue)
        command = input("> ").strip().lower()
        if command == "add":
            add_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "quit":
            is_running = False
            print("The queue is closed. Good night!")
        else:
            print(f"Sorry, I don't know the command '{command}'.")


queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]
run_app(queue)
