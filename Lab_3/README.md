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
  which are **basic and extra food need** of i-th hamster respectively. 0 ≤ H<sub>i</sub>, G<sub>i</sub> ≤ 109
---

##Output
Output contains only one integer - max amount of hamsters you can buy

---

##Algorithm
1. Remove all the hamsters which have `basic food need` bigger than **amount of food we have**.
2. Set `max hamsters amount` to 0
3. Iterate while `max hamsters amount` is less than amount of hamsters. For each iteration do the following:
    + Increase `max hamsters amount` by 1
    + Calculate `total food need` of each hamster as if you bought `max hamsters amount` hamsters
    + Sort hamsters by `total food need`
    + Choose first `max hamsters amount` hamsters with the smallest `total food need`
    + Calculate sum of `total food need` for these hamsters
    + If this sum if bigger than **amount of food we have**: Decrease `max hamsters amount` by 1 and break the cycle

---

## How to run
  + `cd` into folder where you want to store this repository
  + Clone this repository with command `git clone https://github.com/max-dmytryshyn/Algorithms-Labs.git`
  + Choose branch lab_3 with command `git checkout lab_3`
  + Go into folder with files with command `cd Algorithms-Labs`
  + run command `python3 hamsters.py` on Mac/Linux *or* `py hamsters.py` on Windows 
  + input your data from the console according to the template described in **Input** section