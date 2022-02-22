class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> search = new HashSet();
        for(int i =0;i<9;i++){
            for(int j=0;j<9;j++){
                char current_val = board[i][j];
                if(current_val!='.'){
                    if(!search.add(current_val+"found in row"+i)||
                       !search.add(current_val+"found in column"+j)||
                       !search.add(current_val+"found in block"+i/3+"_"+j/3)) return false;
                }
            }
        }
         return true;
    }
}
