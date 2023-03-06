import json
import re


class UniqueStorageCLI:
    def __init__(self):
        self.__users = {}
        self.__current_user = None
        self.__current_container = set()

    def run(self):
        print('Welcome to UniqueStorageCLI!')
        username = input('Please enter your username: ')
        self.switch(username)

        while True:
            print('\nType command. (\'help\' to see all available commands)')
            command = input('> ')
            if command.startswith('help'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    self.print_help()
            elif command.startswith('add'):
                if len(command.split()) == 1:
                    print(f'Too few arguments for this command. Expected: minimum 1, given: {len(command.split()) - 1}')
                else:
                    self.add(*command.split()[1:])
            elif command.startswith('remove'):
                if len(command.split()) == 1:
                    print(f'Too few arguments for this command. Expected: 1, given: {len(command.split()) - 1}')
                elif len(command.split()) > 2:
                    print(f'Too many arguments for this command. Expected: 1, given: {len(command.split()) - 1}')
                else:
                    self.remove(*command.split()[1])
            elif command.startswith('find'):
                self.find(*command.split()[1:])
            elif command.startswith('list'):
                self.list()
            elif command.startswith('grep'):
                if len(command.split()) > 2:
                    print(f'Too many arguments for this command. Expected: 1, given: {len(command.split()) - 1}')
                else:
                    self.grep(*command.split()[1])
            elif command.startswith('save'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    self.save()
            elif command.startswith('load'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    self.load()
            elif command.startswith('switch'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    choice = input(f'Do you want to save your container? (yes/no): ')

                    while choice != 'yes' and choice != 'no':
                        choice = input('Incorrect input! Type \'yes\' or \'no\': ')

                    if choice == 'no':
                        self.__current_container = set()
                    else:
                        print(f'Saving container for {self.__current_user}.')
                    self.__users[self.__current_user] = self.__current_container

                    new_username = input('Please enter the new username: ')
                    self.switch(new_username)
            elif command.startswith('exit'):
                if len(command.split()) > 1:
                    print(f'Too many arguments for this command. Expected: 0, given: {len(command.split()) - 1}')
                else:
                    print('Exiting UniqueStorageCLI. Goodbye!')
                    break
            else:
                print('Unknown command.')

    def print_help(self):
        print('List of commands:\nadd <key> [key, ...] - add one or more elements to the container (if the element '
              'is already in there then don’t add)\nremove <key> - delete key from container\nfind <key> [key, '
              '...] - check if the element is presented in the container, print each found or \'No such elements\' if '
              'nothing is\nlist - print all elements of container\ngrep <regex> - check the value in the container by '
              'regular expression, print each found or \'No such elements\' if nothing is\nsave - save container to '
              'file\nload - load container from file\nswitch - switches to another user\nexit - exit the program')

    def add(self, *keys):
        if keys:
            for key in keys:
                if key not in self.__current_container:
                    self.__current_container.add(key)
            print('Elements were added.')
        else:
            print('There are no elements to add.')

    def remove(self, key):
        if key in self.__current_container:
            self.__current_container.discard(key)
        else:
            print(f'There is no "{key}" in this container. Nothing to remove.')

    def find(self, *keys):
        if keys:
            found = False
            for key in keys:
                if key in self.__current_container:
                    print(key)
                    found = True
            if not found:
                print('No such elements.')
        else:
            print('There is nothing to find.')

    def list(self):
        if self.__current_container:
            print('Container contains:')
            for key in self.__current_container:
                print(key)
        else:
            print('Container contains nothing.')

    def grep(self, regex):
        pattern = re.compile(regex)
        found = False
        for key in self.__current_container:
            if pattern.search(key):
                print(key)
                found = True
        if not found:
            print('No such elements.')

    def save(self):
        filename = f'{self.__current_user}.json'
        with open(filename, 'w') as f:
            json.dump(list(self.__current_container), f)
        print('Container has been saved.')

    def load(self):
        filename = f'{self.__current_user}.json'
        try:
            with open(filename, 'r') as f:
                elements_list = json.load(f)
                for element in elements_list:
                    self.__current_container.add(element)
            print('Container has been loaded.')
        except FileNotFoundError:
            print(f'Cannot load {filename}: file not found.')

    def switch(self, username):
        if username in self.__users:
            choice = input(f'Welcome back, {username}!\nDo you want to load your saved container? (yes/no): ')

            while choice != 'yes' and choice != 'no':
                choice = input('Incorrect input! Type \'yes\' or \'no\': ')

            if choice == 'yes':
                print(f'Loading container for {username}.')
                self.__current_container = self.__users[username]
            else:
                self.__current_container = set()

        else:
            print(f'Hello, {username}. Creating a new container.')
            self.__current_container = set()

        self.__current_user = username
