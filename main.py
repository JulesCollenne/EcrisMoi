import enchant


class Player:
    def __init__(self):
        self.points = 0

    def play(self):
        print("Choose a letter : ")
        while True:
            chosen_letter = input()
            if chosen_letter.isalpha():
                return chosen_letter
            else:
                print("Not a letter !")
                continue


class Game:
    def __init__(self, nb_players):
        self.nb_players = nb_players
        self.players = [Player() for _ in range(self.nb_players)]
        self.board = ""
        self.d = enchant.Dict("fr_FR")
        # self.dictionary = ["bonjour", "salut"]

    def check_win(self):
        for i in range(len(self.board) - 2):
            # if self.board[i:] in self.dictionary:
            if self.d.check(self.board[i:]):
                print(f"Word \"{self.board[i:]}\" completed !")
                return True
        return False

    def run(self):
        end = False
        current_player = 0
        while not end:
            print("\tPlayer " + str(current_player + 1))
            print(self.board)
            self.board += self.players[current_player].play()
            if self.check_win():
                return current_player
            else:
                current_player = (current_player + 1) % self.nb_players


if __name__ == "__main__":
    print("Welcome to Ecrismoi !")
    print("Number of players (max 4) :")
    badInput = True
    nb_players = 0
    while True:
        try:
            nb_players = int(input())
        except ValueError:
            print("Not an integer !")
            continue
        else:
            break
    print(f"Starting game with {nb_players} players...")
    game = Game(nb_players)
    winner = game.run()
    print("Player " + str(winner + 1) + " won !")
