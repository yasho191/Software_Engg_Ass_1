#linked list code for the SE project.

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ssl:
    def __init__(self,n=None):
        """
        initialization of ssl
        n = node
        :param n:
        """
        self.head =  n

    def append(self,n):
        """
        append node to list
        :param n= node:
        :return none:
        """
        temp = self.head
        if temp == None:
            self.head = n
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = n
            print('node is appended...')

    def print(self):
        """
        print the linked list
        :return:
        """
        temp = self.head
        while temp.next != None:
            print(temp.data," ->> ",end='')
            temp = temp.next
        print(temp.data," ->> ")

    def len(self):
        """
        will give len of linked list
        :return count:
        """
        count = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            count += 1
        return count

    def remove(self):
        """
        remove the node
        :return:
        """
        d = int(input())
        temp = self.head
        while d != temp.next.data:
            temp  = temp.next
        pre = temp
        nex = temp.next.next
        pre.next = nex
        print('data removed successfully...')

    def prepend_node(self,n):
        """
        prepend node
        n = node
        :param n:
        :return:
        """
        n.next = self.head
        self.head = n
        print("node is prepended..")

    def add_intermediate(self,n,key):
        """
        add intermediate
        :param n:
        :param key:
        :return:
        """
        if self.search(key):

            temp = self.head
            while temp.data != key:
                temp = temp.next
            n.next , temp.next= temp.next, n

            print("node is inserted..")
        else:
            print("nkey is not found..")

    def search(self,key):
        """
        search in linked list
        :param key:
        :return:
        """
        temp = self.head
        while temp.data!=None:
            print(temp.data)
            if temp.data == key:
                return 1
            else:
                temp = temp.next

        return 0






    



"""
def main():
    t = ssl()
    print('append data..')
    while True:
        data = int(input())
        if data == 0:
            break
        else:
            n = node(data)
            t.append(n)
    print("your ssl is:- ")
    t.print()
    print(t.len())
    t.remove()
    t.print()
    print(t.search(5))
    n = node(4)
    t.add_intermediate(n,3)
    t.print()
    print(t.search(4))
    print(t.search(9))


if __name__ == '__main__':
    main()

"""
