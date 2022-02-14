## Fleiss' Kappa Calculator

Calculator for calculating inter-rater reliability for an arbitrary number of raters using the Fleiss' kappa metric (see Wikipedia: https://en.wikipedia.org/wiki/Fleiss%27_kappa).

### Usage

`python fleiss_kappa.py raters -csv file`, where

- `raters` is an integer representing the number of raters
- `file` is a csv file containing data where each value represents the number of raters who assigned the indicated subject (row) to the indicated column (category), similarly to the example here: https://en.wikipedia.org/wiki/Fleiss%27_kappa#Worked_example except with no row or column metadata or intermediate calculations 
 
