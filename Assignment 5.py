content = '''The quick brown fox jumps over the lazy dog.
Python is a powerful programming language used in web development, data science, and automation.
42 is the answer to life, the universe, and everything.
Tomorrow's weather forecast: Sunny with a chance of code.
Did you know? Bananas are berries, but strawberries aren't!'''

with open("sample.txt", "w") as f1:
    data = "This is the initial content."
    f1.write(data + "\n")

with open("sample.txt", "a") as f2:
    f2.write("\nThis line is appended later.")

with open("sample.txt", "r") as f3:
    read_data = f3.read()
    print("Reading file after writing and appending:")
    print(read_data)

with open("sample.txt", "a+") as f4:
    f4.write("Appending content using a+ mode.\n")
    f4.seek(0)
    new_data = f4.read()
    print("Reading file after append and read:")
    print(new_data)
