# DiamondQuest

A platformer about digging for treasure using *math* drills! It's inspired by
16-bit platformers.

DiamondQuest is an **accessibility-first** platformer, designed to be fun and
completely playable by players with motor disabilities affecting their use of
the mouse or keyboard. There is no "death condition", and no need to worry about
reflexes or tricky combinations: the entire game is playable with *one finger*
on the keyboard, or with a head pointer.

DiamondQuest is also a **math practice game** that coaches you while you solve
math problems. Problem difficulty is determined primarily by how deep you dig,
but the deeper you go, the rarer and more valuable the treasures get.

While most math games try to make practice fun by adding timers and urgency,
DiamondQuest instead gives you all the time you need to solve problems at your
own pace. There's no timers and no way to lose. The more you challenge
yourself, the greater the rewards are!

Featuring original retro graphics, intuitive gameplay, and a relaxing ambient
soundtrack, **DiamondQuest** will challenge everything you ever thought you knew
about platformer games. Get ready for the most fun you've ever had with math.

## Dependencies

DiamondQuest is built with **Python 3.7** and **Wasabi2D**.
See *requirements.txt* for full dependency list.

## Running the Game

You can run the game directly from this repository. If you're on a system
that supports Makefiles, you can simply run `make run`.

Otherwise, create a Python 3.7 virtual environment, and install the package
directly into it, using the following commands from the root of the repository:

``` bash
python3.7 -m venv venv   # create the virtual environment
venv/bin/pip install .   # install the package from the repository
venv/bin/python3 -m diamondquest   # run DiamondQuest in the virtual environment
```

## Credits

DiamondQuest was built as part of GAME MODE 2020, an annual open source event
at MousePaw Media, and during a sprint at EuroPython 2020 Online.
Thanks to everyone who got involved!

MousePaw Media staff is denoted by [brackets].

Programming:

- Harley Davis
- [Wilfrantz Dede]
- [Anna Dunster]
- [Jacob Frazier]
- [Muhammad Adeel Hussain]
- [Elizabeth Larson]
- [Ben Lovy]
- Mohaned Mashaly
- [Jason C. McDonald]: programming lead
- [Graham Mix]

Graphics:

- [Anna R. Dunster]: treasure textures
- [Elizabeth Larson]: miner avatar, splash screen
- Wightking: block textures

Sounds/Music:

- [Jason C. McDonald]: menu music

Educational Design:

- [Jason C. McDonald]
- [Graham Mix]

## Development

To get started on development quickly, we've also provided
*requirements_dev.txt* and a Makefile.

On any system supporting Makefiles, ensure you have Python 3.7 installed,
and then run `make venv-dev` to create the virtual environment with all
required dependencies for development.

See `make help` for the Makefile's other uses.

## Contributions

We do NOT accept pull requests through GitHub.
If you would like to contribute code, please read our
[Contribution Guide][2].

All contributions are licensed to us under the
[MousePaw Media Terms of Development][3].

## License

DiamondQuest is licensed under the BSD-3 License. (See LICENSE.md)

The project is owned and maintained by [MousePaw Media][1].

[1]: https://www.mousepawmedia.com/developers
[2]: https://www.mousepawmedia.com/developers/contribution
[3]: https://www.mousepawmedia.com/termsofdevelopment
