class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):

        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""

        # If the node already exists, update its description
        if event_number in self.nodes:
            self.nodes[event_number].description = description
        else:
            self.nodes[event_number] = StoryNode(event_number, description)

        current = self.nodes[event_number]

        if left_event is not None:
            if left_event not in self.nodes:
                self.nodes[left_event] = StoryNode(left_event, "X")  # Placeholder
            current.left = self.nodes[left_event]

        if right_event is not None:
            if right_event not in self.nodes:
                self.nodes[right_event] = StoryNode(right_event, "X")  # Placeholder
            current.right = self.nodes[right_event]

        if self.root is None:
            self.root = current

    def play_game(self):
        """Interactive function that plays the RPG."""

        if self.root is None:
            print("The game tree is empty!")
            return

        current_node = self.root

        while current_node:
            print(f"\n{current_node.description}")

            if current_node.left is None and current_node.right is None:
                print("End of the story!")
                break

            choice = None
            while choice not in ["1", "2"]:
                print("\nWhat do you want to do next?")
                if current_node.left:
                    print("1. " + current_node.left.description)
                if current_node.right:
                    print("2. " + current_node.right.description)

                choice = input("Enter 1 or 2: ")

            if choice == "1":
                current_node = current_node.left
            else:
                current_node = current_node.right


def load_story(filename, game_tree):
        """Load story from a file and construct the decision tree."""
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) != 4:
                        continue  # Skip invalid lines

                    event_number = int(parts[0])
                    description = parts[1]
                    left_event = int(parts[2]) if parts[2] != "None" else None
                    right_event = int(parts[3]) if parts[3] != "None" else None

                    game_tree.insert(event_number, description, left_event, right_event)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

# Main program
if __name__ == "__main__":
    print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    print("TODO: Start the RPG game")
    game_tree.play_game()
