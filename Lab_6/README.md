# Lab-6

## Task
In search of the Holy Grail, Indiana Jones faced a dangerous trial.
He needs to go through a rectangular corridor, which consists of fragile plates
(recall a scene from the movie "Indiana Jones and the Last Crusade"). 
There is a letter written on each plate:
![](readme_images/corridor_example.png)

He can start from any plate on the left edge. There are 2 exits: the most right
top and bottom plates. (a and f in the example above)

There are 3 rules for Indiana to move:

1.After each step, Indiana must be more right than he was before.
 
![](readme_images/moving_rule_1.png)

2.You can always move to one plate on the right.

![](readme_images/moving_rule_2.png)

3.In addition to moving to one plate to the right, you can jump to any plate
with the same letter if it's on the right. For example, you can jump from the letter a 
to any other the letter a, provided that it's on the right. 

![](readme_images/moving_rule_3.png)

For a given corridor calculate how many ways there are to pass it successfully.

---

## Input
  The input file ijones .in consists of H + 1 lines.
  + The first line contains two numbers W and H, separated by a space: W - width of corridor, 
  H - height of the corridor, 1 ≤ W, H ≤ 2000.
  + Each of the next H lines contains a word with length W, which consists of lowercase Latin letters from a to z.

---

## Output
Output file ijones.out contains only one integer - the number of different ways to pass the corridor.

---

## Algorithm
  Main idea: number of paths to random plate C is a sum of numbers of paths to all plates from which we can get to C.
  With this idea we can build recursive algorithm and with the help of cash of results we can make this algorithm effective 

<b>Complexity = O(W * H)</b>
 
---

## How to run
  + `cd` into folder where you want to store this repository
  + Clone this repository with command `git clone https://github.com/max-dmytryshyn/Algorithms-Labs.git`
  + Choose branch lab_3 with command `git checkout lab_6`
  + Go into folder with files with command `cd Algorithms-Labs/Lab_6`
  + Insert input in a file `ijones.in`
  + Run command `python3 ijones.py` on Mac/Linux or `py ijones.py` on Windows
  + You will get output in `ijones.out`
