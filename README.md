# Pygame Experiment: Tetris
Using reactive programming library Rx and SDL wrapping library pygame to create a simple Tetris game with Python.

To run this program, install dependencies by executing this command: `python -m pip install -r requirements.txt` on your command line
with Python already installed. 

Start the game by running `python main.py`. 

I wrote this up in order to teach myself ReactiveX and reactive programming in general. Reactive programming is a style of programming
that models the problem as a stream of events in time. In this implementation of Tetris, we use pygame to retrieve user input and
the Rx library to create an event stream: A data structure representing a (possibly infinite) sequence of user input. It is then
straightforward to write handlers to these events and subscribe them to the stream. This encourages a very declarative style
of programming and makes it easier to reason about the state of the game. 
