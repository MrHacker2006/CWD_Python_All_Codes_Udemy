def marks(**kwargs):
    # kwargs is a dictionary with all the key value pair passed to marks
    for i in kwargs.keys():
        print(f"The marks of {i} is {kwargs[i]}")

marks(Gautam=99, Gaurav = 49, Saurabh=69, Rudraksh=420)