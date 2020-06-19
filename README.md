<h1 align="center">Military Sim</h1>
<p align="center">CLI military simulator game</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Python-black?style=flat-square&" alt="Made with Python" />
  <!-- <a href="http://makeapullrequest.com/"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="Make a PR" /></a> -->
  <img src="https://img.shields.io/github/license/ninest/military-sim?style=flat-square" alt="MIT" />
  <!-- <a href="https://www.buymeacoffee.com/ninest"><img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat-square" alt="Buy Me A Coffee"></a> -->
</p>


## 🚀 Features
- [x] View soldiers in each vocation (infantry, transport, ...)
  - [x] Have new soldiers join and leave the army each month
  - [x] Pay each soldier depending on their salary from the military's budget
- [ ] Get government support (increased budget) depending on the number of soldiers
- [ ] Have schemes to enlist more people (like voluntary national service)
- [x] Reservists
  - [x] Have reservists leave the army after 10 month
- [ ] Vehicles
- [ ] Calculate the military's preparedness level based on a series of factors:
  - [ ] Number of soldiers
  - [ ] Training quality
  - [ ] Number of vehicles and their power
- [ ] Wars

## 🛠 Build setup
clone or fork the repository. To install all the dependecies, run

```bash
# go into the folder where the code is located
cd src/

# go into python virtual environment
pipenv shell

# install all dependecies
pipenv install
```

Once all dependecies have been installed successfully, run the code with

```
python main.py
```

**Warning**: make sure your command-line window is not too small. Please resize it accordingly if things look weird.


### File setup
- `main.py`: Entry point
- `game.py`: Game loop
- `models/`:
  - Formation model (for each part of the military)
  - Military model (stores all information about the military you control)
  - State (game state, such as rounds played, time game started)
- `utils/`:
  - `displays.py`: custom functions for manipulating terminal content
  - `prompts.py`: custom functions for getting user input

#### main.py
This is the entry point of the game. The user is first shown the title screen, then prompted on what to do. Option 0 (zero) starts the game by calling the `start` function from `game.py`

#### game.py
This is where the military and game state objects are instantiated. The `start` function creates an infinite while loop.

**start (function)**

Each loop iteration in `start` represents a round, or 1 month in game time.

**gameloop (function)**

There's a while loop here to. The loop only breaks when a **choice** has been made successfully. As of now, the choices include
- change enlistment sheme
- change salary (not yet implemented)
- do nothing (end round and do nothing)

After this, some stuff is reset, for example the number of soldiers who joined or left this month. Certain functions are also called, such as those that pay the soldiers their salary (see `Military.month_end` in `models/military.py`)

#### Models

**Military**

The military class is used to store all information about the army:
- number of soldiers in each formation (not sure if "formation" is the right word)
- number of soldiers joined/left this month
- join rate and leave rate (1 by default)
- budget
- government support (how much the government pays the army)

While the join and leave rate are the same initially, it seems like more soldiers are joining the army than leaving. This is because soldiers from the infantry, upon leaving, are still reservists. Reservists are still considered a part of the army. All reservists leave every 10 months.


## 📜 License
MIT