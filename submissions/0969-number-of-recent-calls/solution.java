class RecentCounter {
    
    int counter;
    int arr[] = new int[10000];
    int i=0;

    public RecentCounter() {
        counter=0;
    }
    
    public int ping(int t) {
        arr[i]=t;
        i++;
        int temp=i, count_t=0;
        for(int j=0;j<i;j++)
        {
            if((arr[temp-1]-arr[j])<=3000)
            {
                count_t++;
            }
        }
        this.counter=count_t;
        return this.counter;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
