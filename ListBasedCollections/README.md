## Linked Lists

It's an *<u>ordered</u>* collection of objects.

<img src="file:///Users/mat/Programming/DataStructures/ListBasedCollections/img/list_vs_linked_list.png" title="" alt="" data-align="center">

The order is not given by an index, but by a reference to the next object (**node**)

Every node has two fields: 

- *Value*: the value stored in the list

- *Next*: the reference to the next node

### Performance differences wrt lists

**Insert a new element**

- List
  
  - at the end: using `.append()`, a new element is added with the index *n+1*
     → COMPLEXITY = $O(1)$
  
  - at the beginning: using `.insert()`, the new element will have the index 1, but then all the other elements have to be 'shifted by 1'
    → COMPLEXITY = $O(n)$
  
  <img title="" src="file:///Users/mat/Programming/DataStructures/ListBasedCollections/img/list_insert_beginning.png" alt="" data-align="center" width="565">

- Linked List
  
  - at the end: I have to scroll the entire list, in order to find the last element and then associate to it as 'next' the new node 
    
    → COMPLEXITY = $O(n)$
    
    <img title="" src="file:///Users/mat/Programming/DataStructures/ListBasedCollections/img/linked_list_append.png" alt="" data-align="center" width="567">
  
  - at the beginning: the new node is made the new head, and linked to the previous head. There is no impact on the other nodes
    → COMPLEXITY = $O(1)$
    
    <img title="" src="file:///Users/mat/Programming/DataStructures/ListBasedCollections/img/linked_list_insert_beginning.png" alt="" data-align="center" width="561">
