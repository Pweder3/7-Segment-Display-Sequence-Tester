Simple console app that lets you test different combinations on the display by giving it different binary strings, where each bit calls a separate section of the display high.  


Using this layout 
```
   -- 0 --
  |       |
  5       1
  |       |
   -- 6 --
  |       |
  4       2
  |       |
   -- 3 --
```
   For example,  `"1101111"` would be the digit 9 (note that the program reads right to left so from LSB to MSB)

```
   -------
  |       |
  |       |
  |       |
   -------
          |
          |
          |
   -------
```
