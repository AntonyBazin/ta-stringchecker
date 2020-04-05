# Automata theory task 1

The task solved in 3 ways using different technologies

## 1) RE
Used the re module of Python 3

## 2) SMC
Used the State Machine Compiler to generate code to analyze the strings

## 3) ply
Used the ply package to solve the task

## Test data generation
One can generate the test data using the ```generator.py``` script

## Answer comparison
One can use the ```filecomp.py``` check whether the output files are identical

## Timing
You can use ```gnuplot --persist -e 'plot "[smth]/timing-[smth].txt" u 1:2 with linespoints linestyle 1'```
to plot the timing diagrams

## Meld
You can also use [meld](https://meldmerge.org/) to do the comparison
