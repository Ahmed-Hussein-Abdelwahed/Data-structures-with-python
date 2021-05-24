class Node:
    def __init__(self, element):
        self.data = element
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def first_element(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print(self.first.data)

    def last_element(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print(self.last.data)

    def enqueue(self):
        element = input('Enter an element')
        new_node = Node(element)
        if self.first is None:
            new_node.next = self.last
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        print('Element has been enqueued successfully')

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            self.first = self.first.next
            self.size -= 1
            print('Element has been dequeued successfully')

    def queue_size(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print('Queue contains {} element(s)'.format(self.size))

    def display(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            display_element = self.first
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
            print('\n[1] Queue first')
            print('[2] Queue last')
            print('[3] EnQueue')
            print('[4] Dequeue')
            print('[5] Queue size')
            print('[6] Display')
            print('[7] Terminate')

            user_choice = input()
            if user_choice == '1':
                self.first_element()
            elif user_choice == '2':
                self.last_element()
            elif user_choice == '3':
                self.enqueue()
            elif user_choice == '4':
                self.dequeue()
            elif user_choice == '5':
                self.queue_size()
            elif user_choice == '6':
                self.display()
            elif user_choice == '7':
                break
            else:
                print('Invalid choice ... try again')


queue = Queue()
queue.interface()
