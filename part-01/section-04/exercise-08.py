students = int(input("How many students on the course: "))
desired_group_size = int(input("Desired group size? "))

if students % desired_group_size != 0:
    print(f"Number of groups formed: {students // desired_group_size + 1}")
else:
    print(f"Number of groups formed: {students / desired_group_size}")