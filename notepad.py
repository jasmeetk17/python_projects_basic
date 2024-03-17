import sys
class Notepad:
    def __init__(self,author,file_name) -> None:
        self.author=author
        self._file_name=file_name
    def show_instructions(self):
        print(f" Welcome to the Notepad, {self.author} ")
        print('Commands:')
        print('1- write note')
        print('2- display note')
        print('0- exit notepad')

    def _write_note(self):
        user_input=input('Enter a note: ')
        with open(self._file_name,'a') as note:
            note.write(user_input)

        print('Bot:Note Successfully')

    def _display_note(self):
        try:
            with open(self._file_name,'r') as note:
                text=note.read()
                print(f'Bot:{text}')
        except FileNotFoundError:
            print(f'Bot: you need to write a note first')
    def _exit_notepad(self):
        print(f'See you next time,{self.author}')
        sys.exit()
    def run(self):
        self.show_instructions()
        while True:
            user_input=input(f'{self.author}:')
            if user_input not in ("0","1","2"):
                print('Bot: lease enter a valid choice. ')
                continue

            if user_input=="1":
                self._write_note()
            elif user_input=="2":
                self._display_note()
            elif user_input=="0":
                self._exit_notepad()
            else:
                print(f'Bot: Unknown Command: {user_input}')
notepad=Notepad("Bob","notes.txt")
notepad.run()

