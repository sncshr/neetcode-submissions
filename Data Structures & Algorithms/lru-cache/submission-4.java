public class Node{
    int key;
    int val;
    Node prev;
    Node next;
    public Node(int key, int val)
    {
        this.val=val;
        this.key=key;
    }
}

class LRUCache {
    Node head;
    Node tail;
    HashMap<Integer, Node> cache;
    int capacity;

    public LRUCache(int capacity) {
        this.capacity=capacity;
        cache=new HashMap<>();
        head=new Node(-1,-1);
        tail=new Node(-1,-1);
        this.head.next=this.tail;
        this.tail.prev=this.head;
    }
    private void remove(Node node){
        Node prev=node.prev;
        Node next=node.next;
        prev.next=next;
        next.prev=prev;
    }
    private void insert(Node node){
        Node temp=this.head.next;
        this.head.next=node;
        node.prev=this.head;
        temp.prev=node;
        node.next=temp;
    }
    public int get(int key) {
        if(this.cache.containsKey(key)){
            Node n=this.cache.get(key);
            remove(n);
            insert(n);
            return n.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if(this.cache.containsKey(key)){
            remove(this.cache.get(key));
        }
        Node n= new Node(key,value);
        this.cache.put(key,n);
        insert(n);
        if(this.cache.size()>this.capacity){
            Node toRemove= this.tail.prev;
            remove(toRemove);
            this.cache.remove(toRemove.key);
        }
           
    }
}
