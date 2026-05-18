class MinStack {
    private Stack<Integer> stck;
    private Stack<Integer> minVal;

    public MinStack() {
        stck = new Stack<Integer>();
        minVal= new Stack<>();
    }
    
    public void push(int val) {
        if(!minVal.isEmpty() && minVal.peek()<val){
            stck.push(val);
            minVal.push(minVal.peek());

        }else{
            stck.push(val);
            minVal.push(val);
        }
    }
    
    public void pop() {
        minVal.pop();
        stck.pop();
    }
    
    public int top() {
        return stck.peek();
    }
    
    public int getMin() {
        return minVal.peek();
        
    }
}
