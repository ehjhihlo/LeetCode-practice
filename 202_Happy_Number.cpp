int next_n(int n){
    int r = 0;
    int ans = n;
    int d = 0;
    while(ans != 0){
        d = ans % 10;
        ans = ans / 10;
        r += d*d;
    }
    return r;    
}

bool contain(int* history, int size, int n){
    for(int i=0;i<=size;i++){
        if(history[i]==n){
            return true;
        }
    }
    return false;
}


bool isHappy(int n){
    int history[10000];
    int size = 0;
    while(!contain(history, size, n)){
        history[size]=n;
        size++;
        n = next_n(n);
    }
    return n==1;
}