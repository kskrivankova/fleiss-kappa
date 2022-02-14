import argparse, pathlib
import functools
import csv

parser = argparse.ArgumentParser(description="Calculate the Fleiss kappa")
parser.add_argument("raters", nargs=1, type=int)
parser.add_argument("-csv", nargs=1, type=pathlib.Path, metavar="file_path")

args = vars(parser.parse_args())

if args["raters"][0] < 1:
	raise Exception("Too few raters.")
if args["csv"][0].is_dir():
	raise Exception("Not a file.")
if not args["csv"][0].exists():
	raise Exception("File does not exist.")

matrix = []

with open(args["csv"][0], "r") as f:
	reader = csv.reader(f)

	for row in reader:
		matrix.append(list(map(lambda x: int(x), row)))

num_raters = args["raters"][0]
num_categories = len(matrix[0])
num_subjects = len(matrix)
total = num_raters * num_subjects

proportions = [0] * num_categories
proportions = map(lambda x: x/total, functools.reduce(lambda y, z: map(lambda x: sum(x), zip(y, z)), matrix))
proportions = functools.reduce(lambda x, y: x + y**2, proportions, 0)

coef = (num_raters * (num_raters - 1))
agreement = map(lambda x: (functools.reduce(lambda y, z: y + z**2, x, 0) - num_raters) / coef, matrix)
agreement = sum(agreement) / num_subjects

kappa = (agreement - proportions) / (1 - proportions)
print(f"Number of raters: {num_raters}\nNumber of categories: {num_categories}\nNumer of subjects: {num_subjects}\n")
print(f"Fleiss Kappa: {kappa}")
