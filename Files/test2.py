
with open('test.txt','r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()    # Read all files
    # # f_contents = f.readline()    # Read single line
    # print(f_contents)

    # for line in f:                  # using loop
    #     print(line,end='')

    f_contents = f.read(160)       # Size to read
    print(f_contents)