try:
    my_file = open("names.txt", "r")
    read_file = my_file.read()
except:
    print("An unspecified error has occurred.")
