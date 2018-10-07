import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class nextClosestTime {

	public static void main(String[] args) {
		//System.out.println("ANS: "+closestTimeWithRepetition("22:22"));
		System.out.println("no rep: "+ closestTimeWithoutRepetition("18:00"));
		// TODO Auto-generated method stub

	}
	
	public static String closestTimeWithoutRepetition(String time){
		int minutes = Integer.parseInt(time.substring(0,2)) * 60 + Integer.parseInt(time.substring(3));
		int maxMinutes = 24 * 60;
		List<Integer> allowedDigits = new ArrayList<>();
		for(char i : time.toCharArray()){
			if(i != ':'){
//				System.out.println("Adding: "+ i);
				allowedDigits.add(i - '0');
			}
		}
		int result = minutes;
		for(int i = 0; i<allowedDigits.size(); i++){
//			System.out.println(i+": "+ allowedDigits.get(i));
			for(int j=0;j<allowedDigits.size(); j++){
				if(j == i)
					continue;
//				System.out.println(j+" j: "+ allowedDigits.get(j));
				if((allowedDigits.get(i) * 10 + allowedDigits.get(j)) < 24){
//					System.out.println("i & j: "+ (allowedDigits.get(i) * 10 + allowedDigits.get(j)));
					for(int k = 0;k<allowedDigits.size(); k++){
						if(k == i || k == j)
							continue;
						for(int l = 0;l<allowedDigits.size(); l++){
							if(l == k || l == i || l == j)
								continue;
							if((allowedDigits.get(k) * 10 + allowedDigits.get(l)) < 60){
//								System.out.println("k & l: "+(allowedDigits.get(k) * 10 + allowedDigits.get(l)));
								int checkTime = (allowedDigits.get(i) * 10 + allowedDigits.get(j)) * 60 + (allowedDigits.get(k) * 10 + allowedDigits.get(l));
								int closest = Math.floorMod(checkTime - minutes, 24 * 60);
//								System.out.println(String.format("%02d:%02d", checkTime / 60,  checkTime % 60)+" "+closest);
								if(closest > 0 && closest < maxMinutes){
									result = checkTime;
									maxMinutes = closest;
								}
							}
						}
					}
				}
			
}		}
		return String.format("%02d:%02d", result/60, result%60);
	}
	
	public static String closestTimeWithRepetition(String time){
		int minutes = Integer.parseInt(time.substring(0,2)) * 60 + Integer.parseInt(time.substring(3));
		int maxMinutes = 24 * 60;
		Set<Integer> allowedDigits = new HashSet<>();
		for(int i=0;i<time.length();i++){
			if(time.charAt(i)!=':'){
				allowedDigits.add(time.charAt(i) - '0');
			}
		}
		int result = minutes;
		for(int i: allowedDigits){
			for(int j: allowedDigits){
				if((i *10 + j) < 24){
					for(int k: allowedDigits){
						for(int l: allowedDigits){
							if((k * 10 + l) < 60){
								int checkTime = (i *10 + j) * 60 + (k * 10 + l);
								int close = Math.floorMod(checkTime - minutes, 24 * 60);
								//System.out.println(String.format("%02d:%02d", checkTime/60, checkTime%60)+" && "+checkTime+" "+minutes+" "+ close);
								if(close > 0 && close < maxMinutes){
									result = checkTime;
									maxMinutes = close;
								}
							}
						}
					}
				}
			}
		}
		return String.format("%02d:%02d", result/60, result%60);
	}
}