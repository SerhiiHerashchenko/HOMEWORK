# Guess a number game
**The game consists of 4 modules:**
1. **Computer**
1. **Player**
1. **DataProcessing**
1. **GameProcessing**

### Current game structure

- **Computer module** consists of 2 structures:
    - **Computer interface**, that states basic functionality of ai player, more precisely, the ability to pick the number and check player's move.
    - **ComputerImpl class** that implements previous interface. This class implements methods wich give us posibility to pick a number, check the player's move, and check player's position (winner/ continue to play).
- **Player module** has also 2 structures:
    - **Player interface**, that states the makeMoveConsole() method.
    - **PLayerImpl class**, that implements previous interface, and realize method wich allows player to make move and enter the number.
- **DataProcessing** *has 3 submodules*:
    - **Input module** is composed of two structures:
        - **InputData interface**, that states basic method of data collection.
        - **InputDataConsole class**, that implements InputData methods for console users(players)
    - **Getter module**:
        - **GetData interface**, that states basic method of data returning.
        - **GetDataImpl class** implements method from previous interface, and allows us to return data collected by InputDataConsole method.
    - **Checker module**:
        - **CheckData interface**, that states basic method of checking numbers according to rools.
        - **CheckDataImpl class** implements method from previous interface
- **GameProcessing** is a main class wich implements a game playing simulation.