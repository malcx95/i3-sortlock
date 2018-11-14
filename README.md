# i3-sortlock

This is an i3-lock which takes a screenshot, divides the image into blocks, sorts them, and
locks your screen with the sorted screenshot. It makes your locked computer look broken.

## Example

Screen before locking:
![alt text](https://github.com/malcx95/i3-sortlock/blob/master/images/screen.png)
Screen after locking:
![alt text](https://github.com/malcx95/i3-sortlock/blob/master/images/screen_locked.png)

## Installation and usage

Make sure you have python3, i3lock, scrot, scipy and matplotlib installed.
Clone this repository somewhere, and open `lock.sh` and change line 4 to the absolute 
location of `sortlock.py`. Bind `lock.sh` to some keybinding and you should be good to go!

You can change the block size by changing the `BLOCK_SIZE` constant on line 6 in `sort.py`
(both the height and width of your screen should be divisible by this number). You can
also change what the blocks are to be sorted by, by changing `SORTMETHOD` on line 11. 0 means
sort by hue, 1 by saturation and 2 by value (luminosity).

