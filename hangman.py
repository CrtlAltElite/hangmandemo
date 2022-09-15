import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class LetterBoard():
    MAX_MOVES = 7    
    WORD_BANK = ("microwave","tesla","computer","pineapple","garage","python","bottle",
                "processor","australia","continent","dictionary")

    def __init__(self):
        # Pick a Word
        self.word = LetterBoard.WORD_BANK[random.randint(0,len(LetterBoard.WORD_BANK)-1)] 
        self.guessed_letters = []
        self.number_of_moves = 0
        self.solved = False

    def show_word(self):
        clear_screen()
        board = ["_ " if letter not in self.guessed_letters else letter for letter in self.word]
        for letter in board:
            print(letter, end=" ")
        print()
        print("Guessed Letters: ", end="")
        if self.guessed_letters:
            for letter in self.guessed_letters:
                print(letter, end=" ")
        else:
            print("You haven't guessed yet", end='')
        print()
        print(f"You have {LetterBoard.MAX_MOVES-self.number_of_moves} moves left")

    def guess_letter(self, letter):
        if len(letter)>1:
            print('Invalid guess, must be a single character')
            return
        if letter in self.word:
            count = self.word.count(letter)
            print(f"You found {count} {letter}{'s' if count > 1 else ''}")
        else:
            print(f"{letter} is not in the word")
            self.number_of_moves += 1
        self.guessed_letters.append(letter)
        

    def has_guesses_left(self):
        return self.number_of_moves < LetterBoard.MAX_MOVES

    def guess_word_correct(self, word):
        return word == self.word

    def check_if_all_letters_guessed(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def user_won(self):
        print("Congrats You Solved The Puzzle")
        self.solved=True

    def user_lost(self):
        print("I am SOOOO Sorry You ARe SOOO Bad at this Game.... Why Don't you got HANG YOUSELF!")




class UI():
    def __init__(self):
        self.letter_board = LetterBoard()

    def play_game(self):
        while True:
            # Show Board
            self.letter_board.show_word()
            
            # Ask for a letter
            letter = input("What letter would you like to guess?")

            # Respond with if letter is on the board... if not on the board take away guess or if its on the board revel letter
            self.letter_board.guess_letter(letter)

            # Show Board
            self.letter_board.show_word()

            # Check if the answer was solved by the last guess
            if self.letter_board.check_if_all_letters_guessed():
                #user wins
                self.letter_board.user_won()
                break

            # Let them guess the word
            word_guess = input("Would you like to guess the word? (Y/Yes) ").lower()
            if word_guess == 'y' or word_guess == "yes":
                word = input("What is your guess for the word? ").lower()
                if self.letter_board.guess_word_correct(word):
                    #user wins
                    self.letter_board.user_won()                 
                    break
            # check if the user has any guesses left
            if not self.letter_board.has_guesses_left():
                self.letter_board.user_lost()
                break
            # Repeat steps until solved or lost

def main():
    #Driver Code
    ui = UI()
    ui.play_game()


    
if __name__=="__main__":
    main()
    