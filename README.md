<h1 align="center">Military Sim</h1>
<p align="center">CLI military simulator game</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Python-black?style=flat-square&" alt="Made with Deno" />
  <a href="http://makeapullrequest.com/">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="Make a PR" />
  </a>
  <img src="https://img.shields.io/github/license/ninest/military-sim?style=flat-square" alt="MIT" />
  <a href="https://www.buymeacoffee.com/ninest">
    <img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat-square" alt="Buy Me A Coffee">
  </a>
</p>

Images and GIFs to be added soon.

## 🚀 Features
- [x] View soldiers in each vocation (infantry, transport, ...)
  - [x] Have new soldiers join and leave the army each year
  - [x] Pay each soldier depending on their salary from the military's budget
- [ ] Get government support (increased budget) depending on the number of soldiers
- [ ] Have schemes to enlist more people (like voluntary national service)
- [x] Reservists
  - [x] Have reservists leave the army after 5 years
- [ ] Vehicles
- [ ] Calculate the military's preparedness level based on a series of factors:
  - [ ] Number of soldiers
  - [ ] Training quality
  - [ ] Number of vehicles and their power
- [ ] Wars

## 🛠 Build setup
clone or fork the repository, then run

```
python3 src/main.py
```

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


## 📜 License
MIT