'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(list):
    maximum = max(example_list)
    minimum = min(example_list)
    summ = sum(example_list)
    average = summ / len(example_list)
    print("max: " + str(maximum))
    print("min: " + str(minimum))
    print("sum: " + str(summ))
    print("avg: " + str(average))


# call the function below here
stats(example_list)