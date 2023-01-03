# Keep Talking And Nobody Explode (KTANE)

python3 scritps to solve Keep Talking And Nobody Explode bombes modules.
For now each module on the bombe is solved by a different python script.
The scripts are in the `sources` folder.

## Modules

### Wires ( horizontal )

```sh
python KTANE_horizontal_Wire.py
```
![Alt text](/data/img.jpg?raw=true )

### Button

`` work in progress``
```sh
python KTANE_button.py
```
![Alt text](/data/img.jpg?raw=true )

### Keypads ( symboles )

``For now this module is not supported. Only a graphical implentation would make sense.
Not planned so far.``

### Simon says ( blinking colors )

``For now this module is not supported.``

### Who's on First ( display with 6 words )

``For now this module is not supported``

### Memory ( numbers 1 to 4 )

```sh
python KTANE_memory_game.py
```
![Alt text](/data/img.jpg?raw=true )

### Morse code

``For now this module is not supported``

### Complicated wires ( vertical wires )

```sh
python KTANE_vertical_wire.py
```
![Alt text](/data/KTANE_vertical_wire.jpg?raw=true )

> bsl = blue wire with start and LED 
>
> bws = blue white wire and start 
>
> rl  = red wire and LED 
>
> w   = white wire 


NOTE : CTRL+C out of it ._.

### Wire Sequences ( 1,2,3 A,B,C )

```sh
python KTANE_weird_Wire.py
```
![Alt text](/data/img.jpg?raw=true )

### Maze (naval battle)

``yes, its not a naval batle. too lazy to change it for now ...``
```sh
python KTANE_naval_battle.py
```
![Alt text](/data/KTANE_naval_battle.jpg?raw=true )

> NOTE : the coordinates are given like this :
>
> first the row number
>
> second the line number
>
> starting at 1 ( not 0)


When running the script you're prompted for inputs:
- first provide the map identification ( red circle , 2,4 )
- then  provide the start position ( 6,6 )
- then  provide the stop  position ( 1,1 )

### Passwords

```sh
python KTANE_password.py
```
![Alt text](/data/img.jpg?raw=true )

## Needy modules

None are implemented havent seen them in game yet.
