Assessment Answers:


Runtime ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


1. When calculating the Big O notation for a particular algorithm, it’s necessary to consider the length of time it takes for the algorithm to run as the algorithm’s workload approaches infinity. You can think of the workload as the number of tasks required to complete a job. What determines the workload of figuring out whether your box of animal crackers contains an elephant?

1. ANSWER: THe workload is how many crackers are in the box on animal cookies

2. Order the following runtimes in descending order of efficiency (that is, fastest runtimes first, slowest last) as n approaches infinity:

2. ANSWER: 

O(1)
O(log n)
O(n)
O(n log n)
O(n2)
O(2n) (i.e. 2 to the n-th power)

Stacks and Queues ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

3. In the following cases, would a stack or queue be a more 
                                                appropriate data structure?
A -  The process of loading and unloading pallets onto a flatbed truck 
A - STACK

B - Putting bottle caps on bottles of beer as they roll down an assembly lin 
B - QUEUE

C - Calculating the solution to this mathematical expression: 
                                                    2 + (7 * 4) - (3 / 2)
C - STACK

4.Describe two more situations where a queue would be an appropriate data structure.

4.a ANSWER: Kids lining up to go down the slide (if they are well behaved), first one in line goes down the slide first.
4.b ANSWER: The drive thru at In an Out burger. First one in line get thier burgers first. 

5. Describe two more situations where a stack would be an appropriate data structure.

5.a ANSWER: Claw machine with stuffed animals inside. You woudl want to use the claw to grab the topmost stuffed animal or the one put in last.
5.b ANSWER: To reverse a word. You add lettesr one at a time and then pop letters from the stack

Linked Lists ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

6. Given the linked list below, which are the nodes? What is the data for each node? Where is the head? Where is the tail? (Please be as specific as possible — exactly which parts of the diagram correspond to each part? Arrows? Boxes? Text?)

6. ANSWER: The nodes are the units that contain the stings of data. The data for each node is a string: "Apple" next is "Berry" and next "Cherry" and then None. THe HEAD is the node with the string "Apple" as its data. The TAIL is not indicated in the example shown but I would make the node withthe string "Cherry" as its data the tail of this linked list.

7. What’s the difference between doubly- and singly-linked lists?

7. ANSWER:  Doubly Linked List is a type of Linked list in which traversing  is possible in both ways forwards or backwards. Singly Linked List is a type of Linked list in which traversing is only in directiong, forwards. 

8. Why is it faster to append to a linked list if we keep track of the tail as an attribute?

8. ANSWER: If we keep track of the tail we can easily add tothe end of the list becuase we will have been keeping track of what that is. The slower option would go the entire list one by one to determine what the last item is before we can append to it.

Trees ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

9. Given the tree above, in what order would a Breadth First Search (BFS) algorithm visit each node until finding burrito (starting at food)? Just list the order of nodes visited; no need to recreate the state of the algorithm data in your answer.

9. ANSWER: 
    ORDER: food, Italian, Indian, Mexican, lasagna, pizza, tikka masala, saag, burrito. Burrito found!

10. Given the tree above, in what order would a Depth First Search (DFS) algorithm visit each node until finding Chicago-style (starting at food)? Just list the order of nodes visited; no need to recreate the state of the algorithm data in your answer.

10. ANSWER: 
    ORDER: food, Italian, Indian, Mexican, burrito, tacos, enchiladas, tikka masala, saag, lasagna, pizza, thin crust, Chicago-style. Chicago-style pizza found!

11. How is a binary search tree different from other trees?

11. ANSWER:  this a tree that has both a left and a right child and also has rules for thier arrangement. 