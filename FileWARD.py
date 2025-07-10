def write_file(filename):
    with open(filename, "w") as file:
        file.write("Hello!\n")
        file.write("This is the first line.\n")

def append_file(filename):
    with open(filename, "a") as file:
        file.write("This is an appended line.\n")
        file.write("Appended again! 💛\n")

def read_and_display(filename):
    with open(filename, "r") as file:
        content = file.read()
        print("📄 File Content:")
        print(content)

filename = "example.txt"
write_file(filename)
append_file(filename)
read_and_display(filename)
