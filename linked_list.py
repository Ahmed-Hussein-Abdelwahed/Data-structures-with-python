class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def list_size(self):
        if self.is_empty():
            print('List is empty')
        else:
            print('List size = {}'.format(self.size))

    def push_back(self, item):
        node = Node(item)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        print('Item has been pushed back successfully')

    def push_front(self, item):
        node = Node(item)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        print('Item has been pushed front successfully')

    def insert_at(self, index, item):
        if self.is_empty():
            print('List is empty')
        else:
            node = Node(item)
            insert1 = self.head
            for num in range(int(index) - 1):
                insert1 = insert1.next
            node.next = insert1.next
            insert1.next = node
            self.size += 1
            print('Item has been inserted successfully')

    def erase_at(self, index):
        if self.is_empty():
            print('List is empty')
        else:
            delete1 = self.head
            delete2 = None
            for num in range(int(index) - 1):
                delete2 = delete1
                delete1 = delete1.next
            delete2.next = delete1.next
            del delete1
            self.size -= 1
            print('Item in index {0} has been deleted'.format(index))

    def search(self, item):
        found = False
        if self.is_empty():
            print('list is empty')
        else:
            search_element = self.head
            while search_element:
                if search_element.data == item:
                    print('{0} is found'.format(item))
                    found = True
                    break
                search_element = search_element.next
        if not found:
            print('{0} is not found'.format(item))

    def print_list(self):
        if self.is_empty():
            print('List is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

    def interface(self):
        user_choice = ''
        item = None
        index = None
        while True:
            print('\n', '=' * 80, '[1] Push front', '[2] Insert At', '[3] Push back', '[4] Search', '[5] Erase at',
                  '[6] List size', '[7] Show list items', '[8] Is empty', '[9] Exit  ', sep='\n')
            user_choice = input()
            if user_choice == '1':
                item = input('Enter an item to push front ')
                self.push_front(item)
            elif user_choice == '2':
                index = input('Enter an index to insert ')
                item = input('Enter an item to push front ')
                self.insert_at(index, item)
            elif user_choice == '3':
                item = input('Enter an item to push back ')
                self.push_back(item)
            elif user_choice == '4':
                item = input('Enter an item to search about ')
                self.search(item)
            elif user_choice == '5':
                index = input('Enter an index to erase at ')
                self.erase_at(index)
            elif user_choice == '6':
                self.list_size()
            elif user_choice == '7':
                self.print_list()
            elif user_choice == '8':
                print(self.is_empty())
            elif user_choice == '9':
                break
            else:
                print('Invalid choice ... try again ')


new_list = LinkedList()
new_list.interface()
