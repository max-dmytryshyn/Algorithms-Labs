# Lab-3


## Task
You want to buy hamsters in a pet shop.

Every hamster has two characteristics: **basic food need** which is H *food packages/day*
and **extra food need** which is G *food packages/day* for every other hamster bought.

There are C hamsters in a pet shop. Find **max amount of hamsters** you can buy if you have S
*food packages/day*.


---

##Input
  + First row contain one number S - amount of *food packages/day* you have. 0 ≤ S ≤ 10<sup>9</sup>
  + Second row contain one number C - amount of hamsters in a pet shop. 1 ≤ C ≤ 10<sup>5</sup>
  + The nest C rows contain H<sub>i</sub>, G<sub>i</sub> - two integers, separated with whitespace,
  which are **basic and extra food need** of i-th hamster respectively. 0 ≤ H<sub>i</sub>, G<sub>i</sub> ≤ 10<sup>9</sup>
---

##Output
Output contains only one integer - max amount of hamsters you can buy

---

##Algorithm
1. Remove all the hamsters which have `basic food need` bigger than **amount of food we have**.
2. Create a list of possible hamsters amounts - `possible_amounts`
3. With `possible_amounts` do the following:
    + If length of `possible_amounts` = 0, return 0
    + If length of `possible_amounts` = 1, return this element
    + Choose first `possible amounts[len(possible_amounts) // 2]` hamsters with the smallest `total food need`
    + Calculate sum of `total food need` for these hamsters
    + If this sum < **amount of food we have** return to step 3 with right half of `possible_amounts`
    + Else return to step 3 with left half of `possible_amounts`

<b>Complexity = O(n*log<sup>2</sup>n)</b>
 
---

## How to run
  + `cd` into folder where you want to store this repository
  + Clone this repository with command `git clone https://github.com/max-dmytryshyn/Algorithms-Labs.git`
  + Choose branch lab_3 with command `git checkout lab_3`
  + Go into folder with files with command `cd Algorithms-Labs`
  + run command `python3 hamsters.py` on Mac/Linux *or* `py hamsters.py` on Windows 
  + input your data from the console according to the template described in **Input** section