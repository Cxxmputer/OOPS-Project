class Writer:
    # Initializes instance as soon as they are created.
    def __init__(self, name):
        # Assigning the provided name.
        self.name = name

    def appender(self):
        inquire = input("Do you want to append something to the following file (Y/N)?: ")
        if inquire.lower() == 'y':
            inquire_2 = input('Fine, enter the text: ')
            with open(self.name, 'a') as f:
                f.write(inquire_2)
                print(f'Your text has been appended to {self.name}.')
        elif inquire.lower() == 'n':
            print('Alright, no changes made!')
        # If user enters something else rather than 'Y' and 'N'.
        else:
            print("Something went wrong try again!")

    def writer(self):
        inquire = input("Do you want to overwrite the file or clear the file (Overwrite/Clear): ")
        if inquire.lower() == 'overwrite':
            inquire_2 = input('Enter the text: ')
            with open(self.name, 'w') as f:
                f.write(inquire_2)
                print(f'Your text has been written to {self.name}.')
        elif inquire.lower() == 'clear':
            with open(self.name, 'w') as f:
                f.write("")
                print(f'Your file has been cleared {self.name}.')

    def reader(self):
        # We use 'try and except' for handling errors, an essential approach which avoids program crashing.
        try:
            with open(self.name, 'r') as f:
                print(f.read())
                print(f'File content has been read from {self.name}.')

        except FileNotFoundError:
            print(f'File {self.name} not found!')


file_name = input('Type file name: ')
# Creating an instance of the class 'Writer' with 'file_name' as argument.
myFile = Writer(file_name)  # Passing the 'file_name' as an argument to the class 'Writer', so that it can be assigned to its class attributes.
# Calling the methods (functions inside classes).
myFile.appender()
myFile.writer()
myFile.reader()
