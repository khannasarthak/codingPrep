static int solve3(int [] arr, int k)
	{
		
		int maxIndex = Integer.MIN_VALUE ;
		
		boolean[] set = new boolean[arr.length];
		
		for(int i = 0; i<arr.length; i++)
		{
			
				
			set[arr[i]-1] = true;
		
			if(search(set, k, arr[i]))
			{
				
				maxIndex = Math.max(maxIndex, i+1);
			}
			
		}
		
		return maxIndex == Integer.MIN_VALUE ? -1: maxIndex;
	}
	
static boolean search(boolean[] set, int k, int num)
	{
		//System.out.println(set);
		Boolean pre = null;
		int size = 0;
		int j = 0;
		for(Boolean i: set)
		{
		
			if(pre!=null)
			{
				if(pre!= i )
					{
						if(size==k)
							return true;
						if(i)
							size = 1;
						else
							size =0;
					}
				else if(i)
					size++;
				pre = i;
			}
			else if(i)
			{
				pre = i;
				size++;
			}
		//	if(num ==6)
			//	System.out.println(j +" "+size+" "+i);
	//	j++;
			
		}
		if(size==k)
			return true;
		return false;
	}
