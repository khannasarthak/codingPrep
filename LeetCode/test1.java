import java.util.TreeSet;

public class flowerBloomed {
	
	public static void main(String args[]){
		int arr[] = {12,10,4,7,3,13,2,14,6,11,9,15,8,1,5};
	//	System.out.println(kEmptySlots(arr, 2));
		System.out.println(kFilledSlots(arr, 9));
//		System.out.println(numberOfDigit7(746728));
		
	}
	public static int numberOfDigit7(int n){
		int count = 0;
		while(n>0){
			if(n%10 == 7)
				count++;
			n/= 10;
		}
		return count;
	}

//	public static int kEmptySlots(int[] flowers, int k) {
//        int[] days =  new int[flowers.length];
//        for(int i=0; i<flowers.length; i++)days[flowers[i] - 1] = i + 1;
//        int left = 0, right = k + 1, res = Integer.MAX_VALUE;
//        for(int i = 0; right < days.length; i++){
//            if(days[i] < days[left] || days[i] <= days[right]){
//                if(i == right)res = Math.min(res, Math.max(days[left], days[right]));   //we get a valid subarray
//                left = i; 
//                right = k + 1 + i;
//            }
//        }
//        return (res == Integer.MAX_VALUE)?-1:res;
//    }
//
//	public static int kEmptySlots(int[] flowers, int k) {
//	    int[] days = new int[flowers.length];
//	    for (int i = 0; i < days.length; i++) {
//	        days[flowers[i] - 1] = i + 1;
//	    }
//	    int left = 0;
//	    int right = k + 1;
//	    int res = Integer.MAX_VALUE;
//	    for (int i = 1; right < days.length; i++) {
//	        // current days[i] is valid, continue scanning
//	        if (days[i] > days[left] && days[i] > days[right]) {
//	            continue;
//	        }
//	       // reach boundary of sliding window, since previous number are all valid, record result  
//	        if (i == right) {
//	            res = Math.min(res, Math.max(days[left],days[right]));
//	        }
//	        // not valid, move the sliding window
//	        left = i;
//	        right = left + k + 1;
//	    }
//	    return res == Integer.MAX_VALUE ? -1 : res;
//	}
	
//	public static int kEmptySlots(int[] flowers, int k) {
//        int n = flowers.length;
//        if (n == 0 || k >= n) return -1;
//        int[] f = new int[n + 1];
//        
//        for (int i = 0; i < n; ++i)
//            if (IsValid(flowers[i], k, n, f))
//                return i + 1;
//        
//        return -1;
//    }
//    
//    private static boolean IsValid(int x, int k, int n, int[] f) {
//        f[x] = 1;
//        if (x + k + 1 <= n && f[x + k + 1] == 1) {
//            boolean valid = true; 
//            for (int i = 1; i <= k; ++i)
//                if (f[x + i] == 1) {
//                    valid = false;
//                    break;
//                }
//            if (valid) return true;
//        }
//        if (x - k - 1 > 0 && f[x - k - 1] == 1) {
//            for (int i = 1; i <= k; ++i)
//                if (f[x - i] == 1) return false;
//            return true;
//        }
//        return false;
//    }
	
	public static int kFilledSlots(int[] flowers, int k){
		int n = flowers.length;
        System.out.println("length " + n);
		if(n == 1 && k == 1)
			return 1;
		TreeSet<Integer> sort = new TreeSet<>();
		for(int i=0;i<n;i++){
			sort.add(i+1);
		}
		for(int i = 0;i < n;i++){
			sort.remove(flowers[i]);
			Integer min = sort.lower(flowers[i]);
            System.out.println(i + " min " + min+" for "+flowers[i]);
            Integer max = sort.higher(flowers[i]);
            System.out.println(i + " max " + max);
            if((min != null && max != null  && max - min == k + 1) || (min != null && max == null && n - min == k) || (min == null && max != null && max == k + 1))
            	return i + 1;
		}
		return -1;
	}
	
	public static int kEmptySlots(int[] flowers, int k) {
        int n = flowers.length;
        System.out.println("length " + n);
        if (n == 1 && k == 0) return 1;
        TreeSet<Integer> sort = new TreeSet<>();
        for (int i = 0; i < n; ++i) {
            sort.add(flowers[i]);
            Integer min = sort.lower(flowers[i]);
            System.out.println(i + " min " + min+" for "+flowers[i]);
            Integer max = sort.higher(flowers[i]);
            System.out.println(i + " max " + max);
            int mi = min == null ? -1111111 : min;
            int ma = max == null ? -1111111 : max;
            if (valid(flowers[i], k, mi, ma, flowers.length)) return i + 1;
        }
        return -1;
    }

    static boolean valid(int x, int k, int min, int max, int len) {
    	System.out.println("min: "+min+" max: "+max);
    	if(min == -1111111 && x == k + 1)
    		return true;
    	if(max == -1111111 && len - x == k)
    		return true;
        if (max - x == k + 1)
        	return true;
        if (x - min == k + 1)
        	return true;
        return false;
    }
}