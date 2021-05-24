class Node:
    def __init__(self, element):
        self.data = element
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def stack_top(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            print(self.top.data)

    def push(self):
        element = input('Enter an element to push')
        new_node = Node(element)

        if self.top is None:
            new_node.next = None
        else:
            new_node.next = self.top

        self.top = new_node
        self.size += 1
        print("\nElement has been pushed successfully\n")

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            self.top = self.top.next
            self.size -= 1
            print("\nElement has been popped successfully\n")

    def peak(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            index = input('Enter an index')
            if int(index) > self.size:
                print('Index is out of range')
            elif int(index) <= 0 or not index.isnumeric():
                print('Invalid index')
            else:
                temp = self.top
                counter = 0
                while counter < int(index) - 1:
                    temp = temp.next
                    counter += 1
                print('Position number {} has data = {}'.format(int(index), temp.data))

    def stack_size(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            print(f'Stack contains {self.size} element(s)')

    def display(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            display_element = self.top
            while display_element:
                print(display_element.data, end=' ')
                display_element = display_element.next

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def interface(self):
        while True:
            print('\n[1] Stack top')
            print('[2] Push')
            print('[3] pop')
            print('[4] Peak')
            print('[5] Stack size')
            print('[6] Display elements')
            print('[7] Terminate')
            user_choice = input()
            if user_choice == '1':
                self.stack_top()
            elif user_choice == '2':
                self.push()
            elif user_choice == '3':
                self.pop()
            elif user_choice == '4':
                self.peak()
            elif user_choice == '5':
                self.stack_size()
            elif user_choice == '6':
                self.display()
            elif user_choice == '7':
                break
            else:
                print('Invalid choice ... try again')


stack = Stack()
stack.interface()
