######################################################################################
#
#
#  Name: Samy Masadi
#  Date: 3/22/2019
#
#  This project compares the implementation of a Priority Queue using two different
#  data structures, a heap and a list.  It then measures each module (by time)
#  and prints out the results.  It uses a random number generator to create
#  seven different size lists (10, 50, 500, 1000, 5000, 10000, 50000)
#  to be used for testing.
#
# Once you have your classes working, you will use your PQ_Heap class and PQ_List class
#   to create and compare a rudimentary job scheduler.  
#          1) First, use a random number generator to create your lists.
#             
#          2) Your job scheduler will do the following:
#               start clock
#               enqueue the jobs one at a time 
#               loop until all jobs are complete
#                  looks at top of queue and print it out
#                  Removes 1 job from the queue 
#               stop clock
#
# After you have your time trials complete, create a table in your executive summary
# that lists each module (rows) and time efficiency for worst case (Big O). 
#
#    Further instructions and the rubric is commented into the code below.
#    Leave all comments that we have created intact for grading.
#
####################################################################################
import time
import random

# Class for a priority queue that uses a heap data structure.
class PQ_Heap(object):
    # Constructor for the PQ_Heap
    # Enqueues numbers from a list to create a min heap.
    # Saves heap in list local variable.
    # sampleList: input list of numbers to form initial queue
    def __init__(self, sampleList):
#        print ("creates a min heap from passed in list")
        self.list = []
        for i in range(0, len(sampleList)):
            self.enQueueNP(sampleList[i])
#      
#        Create a min heap from passed in list - return the min heap (10 points)

    # Enqueues with No Print.
    # A single number is added to the end of the heap.
    # Then sift the number up the heap: if it is less than its parent, swap
    # item: the number to enqueue
    # Returns the final index of the item added.
    def enQueueNP(self, item):
        self.list.append(item)
        index = len(self.list) - 1
        heap = False
        while not heap:
            parent = (index - 1) // 2
            if parent >= 0:
                if self.list[parent] > self.list[index]:
                    self.list[parent], self.list[index] = self.list[index], self.list[parent]
                    index = parent
                else:
                    heap = True
            else:
                heap = True
        return index

    # Enqueue with print statements.
    # It calls enqueue for a single number,
    # but will also print the item's parent and children, if any.
    # item: the number to enqueue
    # file: the file to write print statements to
    def enQueue(self, item, file):
#        print ("adds an item to the PQ and reheapifies")
        index = self.enQueueNP(item)
        parent = (index - 1) // 2           # Parent index
        if parent >= 0:                     # Check if parent exists.
            file.write("Parent: {:d}\n".format(self.list[parent]))
        else:
            file.write("Parent: n/a\n")
        child1 = 2 * index + 1              # Left child index
        child2 = 2 * index + 2              # Right child index
        if child1 < len(self.list):         # Check if left child exists.
            if child2 < len(self.list):     # Check if right child exists.
                file.write("Children: {:d}, {:d}\n".format(self.list[child1], self.list[child2]))
            else:
                file.write("Children: {:d}\n".format(self.list[child1]))
        else:
            file.write("Children: n/a\n")
#
#        Add an item to the PQ and reheapify. Print out parent and children (if applicable)
#        or n/a if not (10 points)

    # Dequeues the highest priority item from the min heap.
    # Swap the first item in the list with the last.
    # Pop the last element to remove highest priority item and resize the list.
    # Reheapify by sifting the first element down:
    # Check children, if any. If it is greater than any children, swap with the smallest child.
    # Keep sifting until no children left, or it smaller than its children.
    def deQueue(self):
#        print ("removes the highest priority item from the PQ and reheapifies")
        last = len(self.list) - 1
        self.list[0], self.list[last] = self.list[last], self.list[0]
        self.list.pop()
        index = 0
        heap = False
        while not heap:
            child1 = 2 * index + 1              # Left child index
            child2 = 2 * index + 2              # Right child index
            if child1 < len(self.list):         # Check if left child exists.
                if child2 < len(self.list):     # Check if right child exists.
                    if self.list[child1] <= self.list[child2]:
                        if self.list[child1] < self.list[index]:
                            self.list[index], self.list[child1] = self.list[child1], self.list[index]
                            index = child1
                        else:
                            heap = True
                    else:
                        if self.list[child2] < self.list[index]:
                            self.list[index], self.list[child2] = self.list[child2], self.list[index]
                            index = child2
                        else:
                            heap = True
                else:
                    if self.list[child1] < self.list[index]:
                        self.list[index], self.list[child1] = self.list[child1], self.list[index]
                        index = child1
                    else:
                        heap = True
            else:
                heap = True
#
#       Remove the highest priority item from the PQ and reheapify (10 points)

    # Returns the current highest priority item in the heap,
    # which should always be the first element in the list.
    def sneakAPeek(self):
#        print ("returns the highest priority in the PQ, but does not remove it")
        return self.list[0]
#
#       Return the highest priority item from the PQ, but don't remove it (2 points)

    # Checks to see if the queue has no items.
    # Returns True if empty, False if the queue has entries.
    def isEmpty(self):
#        print ("returns T if PQ is empty, F if PQ has entries")
        if len(self.list) > 0:
            return False
        else:
            return True
#
#       Return a T if PQ is empty, F if PQ is not empty (2 points)

    # Returns the current length of the queue using Python len() function.
    def size(self):
#        print ("returns number of items in queue")
        return len(self.list)

#       Return the number of items in the queue (2 points)

# Class for a priority queue that uses an unsorted list structure.
class PQ_List(object):
    # Initializes the priority queue by copying the input list to the object's list variable.
    # sampleList: the input list of numbers to form initial queue
    def __init__(self, sampleList):
#        print ("creates an unsorted list from passed in list")
        self.list = sampleList.copy()
#      
#        Returns the list (2 points)

    # Enqueues a single item to the end of the queue.
    # As it is an unsorted list, it will have no parents or children.
    # item: the number to enqueue
    # file: the file to write to
    def enQueue(self, item, file):
#        print ("adds an item to the PQ")
        self.list.append(item)
        file.write("Parent: n/a\n")    # Print statements included for apples-to-apples
        file.write("Children: n/a\n")  # execution time comparison to heap enQueue.

#       Add an item to the PQ (5 points)

    # Dequeues the highest priority item from the queue.
    # It must search through the whole list,
    # find the highest priorty item, then remove it.
    # Swap it with the last element, then pop the last element to remove it and resize the list.
    def deQueue(self):
#        print ("removes the highest priority item from the PQ")
        if len(self.list) > 1:
            smallest = 0        
            for i in range(1, len(self.list)):
                if self.list[i] < self.list[smallest]:
                    smallest = i
            self.list[smallest], self.list[-1] = self.list[-1], self.list[smallest]
            self.list.pop()
        elif len(self.list) == 1:
            self.list.pop()

#       Remove the highest priority item from the PQ (5 points)

    # Returns the highest priority item in the queue.
    # Must search through the entire list to find the highest priority item,
    # and then return it.
    def sneakAPeek(self):
#        print ("returns the highest priority in the PQ, but does not remove it")
        if len(self.list) > 1:
            smallest = 0        
            for i in range(1, len(self.list)):
                if self.list[i] < self.list[smallest]:
                    smallest = i
            return self.list[smallest]
        elif len(self.list) == 1:
            return self.list[0]
#
#       Return the highest priority item from the PQ, but don't remove it (2 points)

    # Check whether the queue currently has no items.
    # Call Python len function on list then compare to zero.
    # Returns True if empty, False if it contains items.
    def isEmpty(self):
#        print ("returns T if PQ is empty, F if PQ has entries")
        if len(self.list) > 0:
            return False
        else:
            return True
#        
#       Return a T if PQ is empty, F if PQ is not empty (2 points)

    # Use Python len function on list variable.
    # Return the current number of items in the queue.
    def size(self):
#        print ("returns number of items in queue")
        return len(self.list)

#       Return the number of items in the queue (2 points)

# Function to construct a list of random integers between (1-50000).
# arr: the list to populate with numbers
# length: the desired final length of the list
def randomList(arr, length):
    for i in range(0, length):
        arr.append(random.randint(1, 50000))

# Function to simulate a basic job scheduler using PQ_Heap.
# Enqueues items from an input list by constructing the heap-based queue.
# Then Dequeues highest priority items, one at a time, until queue is empty.
# file: the file to write jobs as they are dequeued.
# arr: the input list of numbers to form the queue.
def heap_scheduler(file, arr):
    my_heapPQ = PQ_Heap(arr)
    file.write("DeQueue Order:\n\n")
    printed = 0
    while not my_heapPQ.isEmpty():
        file.write(str(my_heapPQ.sneakAPeek()))
        printed += 1
        my_heapPQ.deQueue()
        if not my_heapPQ.isEmpty():
            file.write(",")
            if printed % 25 == 0:
                file.write("\n")
    file.close()

# Function to simulate a basic job scheduler using PQ_List.
# Enqueues items from an input list by constructing the list-based queue.
# Then Dequeues highest priority items, one at a time, until queue is empty.
# file: the file to write jobs as they are dequeued.
# arr: the input list of numbers to form the queue.
def list_scheduler(file, arr):
    my_listPQ = PQ_List(arr)
    file.write("DeQueue Order:\n\n")
    printed = 0
    while not my_listPQ.isEmpty():
        file.write(str(my_listPQ.sneakAPeek()))
        printed += 1
        my_listPQ.deQueue()
        if not my_listPQ.isEmpty():
            file.write(",")
            if printed % 25 == 0:
                file.write("\n")
    file.close()    

#Use a pseudo random number generator to generate 7 different size lists (10 points)    
print ("Create 7 lists of different sizes (10, 50, 500, 1000, 5000, 10000, 50000) to use for testing.")
print ("Use a pseudo random number generator to generate lists (1-50000)")

print ("Then time each module as it uses each list and print")
print ("out results in a table")

#change this code to create lists as described above and time each function
nums10 = []
randomList(nums10, 10)
nums50 = []
randomList(nums50, 50)
nums500 = []
randomList(nums500, 500)
nums1000 = []
randomList(nums1000, 1000)
nums5000 = []
randomList(nums5000, 5000)
nums10000 = []
randomList(nums10000, 10000)
nums50000 = []
randomList(nums50000, 50000)

### Create report files for module performance results. ###
r10 = open("report10.txt", "w")
r50 = open("report50.txt", "w")
r500 = open("report500.txt", "w")
r1000 = open("report1000.txt", "w")
r5000 = open("report5000.txt", "w")
r10000 = open("report10000.txt", "w")
r50000 = open("report50000.txt", "w")

#sampleList = open("sample_queue.txt", "r")

#For each module, start the clock, call module, stop clock

# Function to test all modules in PQ_Heap and PQ_List.
# Time each module in seconds then write a report of the results to a file.
# file: the file to write performance report to
# arr: the input list to construct the priority queues from
def comparePQ(file, arr):
    file.write("Heap vs. List Performance Report\n")
    file.write("Number of items: {:d}\n\n".format(len(arr)))
    # Test PQ_Heap init
    start = time.perf_counter()
    my_heapPQ = PQ_Heap(arr)
    end = time.perf_counter()
    heap_time = end - start

    file.write("Heap initialized.\n")
    file.write("Contents: ") #print first 10 numbers, use size to prove the rest is there
    for i in range(0, 10):
        file.write(str(my_heapPQ.list[i]))
        if i < 9:
            file.write(", ")
        else:
            if len(arr) > 10:
                file.write("...")
            file.write("\n")
    file.write("Size: {:d}\n\n".format(my_heapPQ.size()))
    # Test heap enQueue
    file.write("EnQueue item of priority 1500.\n")
    start = time.perf_counter()
    my_heapPQ.enQueue(1500, file)
    end = time.perf_counter()
    heap_enQ_time = end - start
    file.write("EnQueue item completed.\n")
    # Test heap deQueue
    start = time.perf_counter()
    my_heapPQ.deQueue()
    end = time.perf_counter()
    heap_deQ_time = end - start
    file.write("DeQueue highest priority item completed.\n")
    # Test heap sneakAPeek
    start = time.perf_counter()
    my_heapPQ.sneakAPeek()
    end = time.perf_counter()
    heap_peek_time = end - start
    file.write("Peak at highest priority item completed.\n")
    # Test heap isEmpty
    start = time.perf_counter()
    my_heapPQ.isEmpty()
    end = time.perf_counter()
    heap_empty_time = end - start
    file.write("Check for empty queue completed.\n")
    # Test heap size
    start = time.perf_counter()
    my_heapPQ.size()
    end = time.perf_counter()
    heap_size_time = end - start
    file.write("Check size completed.\n\n")
    # Test PQ_List init
    start = time.perf_counter()
    my_listPQ = PQ_List(arr)
    end = time.perf_counter()
    list_time = end - start

    file.write("List initialized.\n")
    file.write("Contents: ") #print first 10 numbers, use size to prove the rest is there
    for i in range(0, 10):
        file.write(str(my_listPQ.list[i]))
        if i < 9:
            file.write(", ")
        else:
            if len(arr) > 10:
                file.write("...")
            file.write("\n")
    file.write("Size: {:d}\n\n".format(my_listPQ.size()))
    # Test list enQueue
    file.write("EnQueue item of priority 1500.\n")
    start = time.perf_counter()        
    my_listPQ.enQueue(1500, file)
    end = time.perf_counter()
    list_enQ_time = end - start
    file.write("EnQueue item completed.\n")
    # Test list deQueue
    start = time.perf_counter()
    my_listPQ.deQueue()
    end = time.perf_counter()
    list_deQ_time = end - start
    file.write("DeQueue highest priority item completed.\n")
    # Test list sneakAPeek
    start = time.perf_counter()
    my_listPQ.sneakAPeek()
    end = time.perf_counter()
    list_peek_time = end - start
    file.write("Peek at highest priority item completed.\n")
    # Test list isEmpty
    start = time.perf_counter()
    my_listPQ.isEmpty()
    end = time.perf_counter()
    list_empty_time = end - start
    file.write("Check for empty queue completed.\n")
    # Test list size
    start = time.perf_counter()
    my_listPQ.size()
    end = time.perf_counter()
    list_size_time = end - start
    file.write("Check size completed.\n\n")
    # Results table
    file.write("Performance Results Table (measurements in seconds)\n")
    file.write("{:^10}{:^10}{:^10}\n".format("Module", "Heap", "List"))
    file.write("{:10}{:10.6f}{:10.6f}\n".format("__init__", heap_time, list_time))
    file.write("{:10}{:10.6f}{:10.6f}\n".format("enQueue", heap_enQ_time, list_enQ_time))
    file.write("{:10}{:10.6f}{:10.6f}\n".format("deQueue", heap_deQ_time, list_deQ_time))
    file.write("{:10}{:10.6f}{:10.6f}\n".format("sneakAPeek", heap_peek_time, list_peek_time))
    file.write("{:10}{:10.6f}{:10.6f}\n".format("isEmpty", heap_empty_time, list_empty_time))
    file.write("{:10}{:10.6f}{:10.6f}\n".format("size", heap_size_time, list_size_time))

    file.close()

### Module performance tests on lists of various sizes. ###
# With console print statements to show progress of program.
print("Module testing...")
comparePQ(r10, nums10)
print("Size 10 results saved to report10.txt")
comparePQ(r50, nums50)
print("Size 50 results saved to report50.txt")
comparePQ(r500, nums500)
print("Size 500 results saved to report500.txt")
comparePQ(r1000, nums1000)
print("Size 1000 results saved to report1000.txt")
comparePQ(r5000, nums5000)
print("Size 5000 results saved to report5000.txt")
comparePQ(r10000, nums10000)
print("Size 10000 results saved to report10000.txt")
comparePQ(r50000, nums50000)
print("Size 50000 results saved to report50000.txt")

#Time each module for each list, and print the results in a table
# (rows - modules, columns - heap, list) (10 points)

### Heap Job Scheduler Testing ###
print("Heap job scheduler testing...")
h_s10 = open("heap_scheduler10.txt", "w")
h_s50 = open("heap_scheduler50.txt.", "w")
h_s500 = open("heap_scheduler500.txt", "w")
h_s1000 = open("heap_scheduler1000.txt", "w")
h_s5000 = open("heap_scheduler5000.txt", "w")
h_s10000 = open("heap_scheduler10000.txt", "w")
h_s50000 = open("heap_scheduler50000.txt", "w")

start = time.perf_counter()
heap_scheduler(h_s10, nums10)
end = time.perf_counter()
h_s10_time = end - start
print("Heap scheduling progress for size 10 saved to heap_scheduler10.txt")

start = time.perf_counter()
heap_scheduler(h_s50, nums50)
end = time.perf_counter()
h_s50_time = end - start
print("Heap scheduling progress for size 50 saved to heap_scheduler50.txt")

start = time.perf_counter()
heap_scheduler(h_s500, nums500)
end = time.perf_counter()
h_s500_time = end - start
print("Heap scheduling progress for size 500 saved to heap_scheduler500.txt")

start = time.perf_counter()
heap_scheduler(h_s1000, nums1000)
end = time.perf_counter()
h_s1000_time = end - start
print("Heap scheduling progress for size 1000 saved to heap_scheduler1000.txt")

start = time.perf_counter()
heap_scheduler(h_s5000, nums5000)
end = time.perf_counter()
h_s5000_time = end - start
print("Heap scheduling progress for size 5000 saved to heap_scheduler5000.txt")

start = time.perf_counter()
heap_scheduler(h_s10000, nums10000)
end = time.perf_counter()
h_s10000_time = end - start
print("Heap scheduling progress for size 10000 saved to heap_scheduler10000.txt")

start = time.perf_counter()
heap_scheduler(h_s50000, nums50000)
end = time.perf_counter()
h_s50000_time = end - start
print("Heap scheduling progress for size 50000 saved to heap_scheduler50000.txt")

### List Job Scheduler Testing ###
print("List job scheduler testing...")
l_s10 = open("list_scheduler10.txt", "w")
l_s50 = open("list_scheduler50.txt.", "w")
l_s500 = open("list_scheduler500.txt", "w")
l_s1000 = open("list_scheduler1000.txt", "w")
l_s5000 = open("list_scheduler5000.txt", "w")
l_s10000 = open("list_scheduler10000.txt", "w")
l_s50000 = open("list_scheduler50000.txt", "w")

start = time.perf_counter()
list_scheduler(l_s10, nums10)
end = time.perf_counter()
l_s10_time = end - start
print("List scheduling progress for size 10 saved to list_scheduler10.txt")

start = time.perf_counter()
list_scheduler(l_s50, nums50)
end = time.perf_counter()
l_s50_time = end - start
print("List scheduling progress for size 50 saved to list_scheduler50.txt")

start = time.perf_counter()
list_scheduler(l_s500, nums500)
end = time.perf_counter()
l_s500_time = end - start
print("List scheduling progress for size 500 saved to list_scheduler500.txt")

start = time.perf_counter()
list_scheduler(l_s1000, nums1000)
end = time.perf_counter()
l_s1000_time = end - start
print("List scheduling progress for size 1000 saved to list_scheduler1000.txt")

start = time.perf_counter()
list_scheduler(l_s5000, nums5000)
end = time.perf_counter()
l_s5000_time = end - start
print("List scheduling progress for size 5000 saved to list_scheduler5000.txt")

print("Now scheduling size 10000 list. This will take several seconds...")
start = time.perf_counter()
list_scheduler(l_s10000, nums10000)
end = time.perf_counter()
l_s10000_time = end - start
print("List scheduling progress for size 10000 saved to list_scheduler10000.txt")

print("Now scheduling size 50000 list. This will take several minutes...")
start = time.perf_counter()
list_scheduler(l_s50000, nums50000)
end = time.perf_counter()
l_s50000_time = end - start
print("List scheduling progress for size 50000 saved to list_scheduler50000.txt")
print("Tests completed! Thanks for your patience!")

### Write Job Scheduler Test Results to File ###
results = open("scheduler_results.txt", "w")
results.write("Job Scheduler Test Results\n")
results.write("Time measurements are in seconds.\n\n")
results.write("{:^10}{:^10}{:^10}\n".format("Size", "Heap", "List"))
results.write("{:10}{:10.6f}{:10.6f}\n".format("10", h_s10_time, l_s10_time))
results.write("{:10}{:10.6f}{:10.6f}\n".format("50", h_s50_time, l_s50_time))
results.write("{:10}{:10.6f}{:10.6f}\n".format("500", h_s500_time, l_s500_time))
results.write("{:10}{:10.6f}{:10.6f}\n".format("1000", h_s1000_time, l_s1000_time))
results.write("{:10}{:10.6f}{:10.6f}\n".format("5000", h_s5000_time, l_s5000_time))
results.write("{:10}{:10.6f}{:10.6f}\n".format("10000", h_s10000_time, l_s10000_time))
results.write("{:10}{:10.6f}{:10.5f}\n".format("50000", h_s50000_time, l_s50000_time))
results.close()
print("Job scheduler test results written to scheduler_results.txt")

#Time both your schedulers and print out results for each here (5 points)

### Generate Time Efficiency Report File ###
c_file = open("complexity_report.txt", "w")
c_file.write("Priority Queue Module Time Efficiency\n\n")
c_file.write("{:11}{:10}{:10}\n".format("Module", "Heap", "List"))
c_file.write("{:11}{:10}{:10}\n".format("__init__", "O(nlogn)", "O(n)"))
c_file.write("{:11}{:10}{:10}\n".format("enQueue", "O(logn)", "O(1)"))
c_file.write("{:11}{:10}{:10}\n".format("deQueue", "O(logn)", "O(n)"))
c_file.write("{:11}{:10}{:10}\n".format("sneakAPeek", "O(1)", "O(n)"))
c_file.write("{:11}{:10}{:10}\n".format("isEmpty", "O(1)", "O(1)"))
c_file.write("{:11}{:10}{:10}\n".format("size", "O(1)", "O(1)"))
c_file.write("{:11}{:10}{:10}\n".format("scheduler", "O(nlogn)", "O(n^2)"))
c_file.close()
print("Time efficiency report saved to complexity_report.txt")
print()
print("Program complete.")

#Once you have your time trials complete, create a table that lists each module (rows)
#and time efficiency for worst case (Big O) and print here (and include in your executive summary. (10 points)  
