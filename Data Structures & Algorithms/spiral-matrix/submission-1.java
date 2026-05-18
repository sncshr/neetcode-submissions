class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m=matrix[0].length;
        int n=matrix.length;
        int left=0;
        int right=m;
        int top=0;
        int bottom=n;
        List<Integer> retArr= new ArrayList<>();        
        while (left<right && top<bottom){
            for(int i=left;i<right;i++){
                retArr.add(matrix[top][i]);
            }
            top+=1;
            for(int i=top;i<bottom;i++){
                retArr.add(matrix[i][right-1]);
            }
            right-=1;
            if (!(top<bottom && left<right)) break;
            for (int i=right-1;i>=left;i--){
                retArr.add(matrix[bottom-1][i]);
            }
            bottom-=1;
            for (int i=bottom-1;i>=top;i--){
                retArr.add(matrix[i][left]);
            }
            left+=1;

        }
        return retArr;
    }
}
