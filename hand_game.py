#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


class HumanPlayer(Player):
    def move(self):
        self.my_move = input("Rock, paper, or scissors?\n").lower()
        while True:
            if "rock" in self.my_move:
                return("rock")
            elif "paper" in self.my_move:
                return("paper")
            elif "scissors" in self.my_move:
                return("scissors")
            else:
                print("Sorry, not a valid response, try agains")
                self.my_move = input(
                    "Rock, paper, or scissors?\n").lower()


class ReflectPlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1.score += 1
            print("Player 1 won this round!")
            print(f"The score is Player One {self.p1.score} to "
                  f"Player Two {self.p2.score}")
        elif beats(move2, move1) is True:
            self.p2.score += 1
            print("Player 2 won!")
        else:
            print("It was a tie ")
            print(f"The score is Player One {self.p1.score} to "
                  f"Player Two {self.p2.score}")

    def play_game(self):
        print("Game start!")
        self.p1.score = 0
        self.p2.score = 0
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()

        if self.p1.score > self.p2.score:
            print("Player One wins the game.")
        elif self.p1.score < self.p2.score:
            print("Player Two wins the game.")
        else:
            print("It is a tie!")

        print("Game over!")


players = (ReflectPlayer(), RandomPlayer(), CyclePlayer())
random_players = random.choice(players)


if __name__ == '__main__':
    game = Game(HumanPlayer(), random_players)
    game.play_game()
