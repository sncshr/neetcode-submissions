class Solution {
    public void rotate(int[][] matrix) {
        int n=matrix.length;

        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<((int)(n/2));j++){
                System.out.println(i);
                int temp=matrix[i][j];
                matrix[i][j]=matrix[i][n-1-j];
                matrix[i][n-1-j]=temp;
            } 
        }

        // int left=0;
        // int right=n-1;
        // while(left<right){
        //     for(int i=0;i<(right-left);i++){
        //         int top=left;
        //         int bottom=right;
        //         int topLeft= matrix[top][left+i];
        //         matrix[top][left+i]=matrix[bottom-i][left];
        //         matrix[bottom-i][left]=matrix[bottom][right-i];
        //         matrix[bottom][right-i]=matrix[top+i][right];
        //         matrix[top+i][right]=topLeft;
        //     }
        //     left++;
        //     right--;
        // }
    }
}
