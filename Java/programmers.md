### 햄버거 만들기

```java
import java.util.Stack;
class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        while (i<ingredient.length) {
            stack.push(ingredient[i]);
            int s = stack.size();
            if (s >= 4 && stack.get(s-1) == 1 && stack.get(s-2) == 3 && stack.get(s-3) == 2 && stack.get(s-4) == 1) {
                stack.pop();
                stack.pop();
                stack.pop();
                stack.pop();
                answer ++;
            }
            i++;
        }
        
        return answer;
    }
}
```

### 나머지가 1이 되는 수 찾기

```java
class Solution {
    public int solution(int n) {
        int answer = 1;
        
        while (answer < n) {
            if (n%answer == 1) {
                return answer;
            }
            answer ++;
        }  
        return answer;
    }
}
```

### 없는 숫자 더하기

```java
import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        int[] arr = new int[10];
        for (int i=0;i<numbers.length;i++) {
            arr[numbers[i]] = 1;
        }
        
        for (int i=0;i<10;i++) {
            if (arr[i] == 0) {
                answer += i;
            }
        }
        return answer;
    }
}
```

### 부족한 금액 계산하기

```java
import java.lang.Math;
class Solution {
    public long solution(int price, int money, int count) {
        long nCount = count*(count+1)/2;
        return Math.max(nCount*price-money,0);
    }
}
```

### 시저암호

``` java
class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for (char ch: s.toCharArray()) {
            if (ch == ' ') {
                answer += ch;
            } else if (ch >= 'a' && ch <= 'z'){
                answer += (char)('a' + (ch+n-'a')%26);
            } else {
                answer += (char)('A' + (ch+n-'A')%26);
            }
        }
        
        return answer;
    }
}
```

### 최소직사각형

```java
import java.lang.Math;
class Solution {
    public int solution(int[][] sizes) {
        
        int maxV = 0;
        int minMaxV = 0;
        
        for (int[] a: sizes) {
            if (maxV < Math.max(a[0],a[1])) {
                maxV = Math.max(a[0],a[1]);
            }
            
            if (minMaxV < Math.min(a[0],a[1])) {
                minMaxV = Math.min(a[0],a[1]);
            }
        }
        return maxV*minMaxV;
    }
}
```

### 삼총사

```java
class Solution {
    public int solution(int[] number) {
        int answer = 0;
        
        for (int n=0;n<number.length;n++) {
            for (int m=n+1;m<number.length;m++) {
                for (int l=m+1;l<number.length;l++) {
                    if (number[n]+number[m]+number[l] == 0) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}
```

### 2016년

```java
import java.util.HashMap;
class Solution {
    public String solution(int a, int b) {
        String answer = "";
        HashMap<Integer,String> days = new HashMap<>();
        days.put(3,"MON");
        days.put(4,"TUE");
        days.put(5,"WED");
        days.put(6,"THU");
        days.put(0,"FRI");
        days.put(1,"SAT");
        days.put(2,"SUN");
        
        
        HashMap<Integer,Integer> calendar = new HashMap<>();
        calendar.put(1,31);
        calendar.put(2,29);
        calendar.put(3,31);
        calendar.put(4,30);
        calendar.put(5,31);
        calendar.put(6,30);
        calendar.put(7,31);
        calendar.put(8,31);
        calendar.put(9,30);
        calendar.put(10,31);
        calendar.put(11,30);
        calendar.put(12,31);
        
        int tmp = 0;
        for (int i=1;i<a;i++) {
            tmp += calendar.get(i);
        }
        int residue = (tmp+b-1)%7;
        
        return days.get(residue);
    }
}
```

### 소수만들기

```java
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int[] primes = new int[3001];
        
        for (int i=2;i<primes.length;i++) {
            if (primes[i] == 0) {
                primes[i] = 1;
                for (int j=2;i*j<primes.length;j++) {
                    primes[i*j] = 2;
                }
            }
        }
        
        for (int i=0;i<nums.length;i++) {
            for (int j=i+1;j<nums.length;j++) {
                for (int l=j+1;l<nums.length;l++) {
                    if (primes[nums[i]+nums[j]+nums[l]]==1) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}
```

### 숫자 짝꿍

```java
import java.lang.*;
import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        StringBuilder builder = new StringBuilder();
        int[] arrX = new int[10];
        int[] arrY = new int[10];
        for (Character s:X.toCharArray()) {
            arrX[Character.getNumericValue(s)]++;
        }
        for (Character s:Y.toCharArray()) {
            arrY[Character.getNumericValue(s)]++;
        }

        for (int i=9;i>=0;i--) {
            if (arrX[i]>0 && arrY[i]>0) {
                builder.append(String.valueOf(i).repeat(Math.min(arrX[i],arrY[i])));
            }
        }
        if (builder.length() == 0) {
            return "-1";
        } else if (builder.charAt(0) == '0') {
            return "0";
        }

        return builder.toString();
    }
}
```

## Level2

### 귤고르기

```java
import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int t:tangerine) {
            if (map.containsKey(t)) {
                map.put(t,map.get(t)+1);
            } else {
                map.put(t,1);
            }
        }
        
        
        List<Map.Entry<Integer,Integer>> entryList = new ArrayList<>(map.entrySet());
        entryList.sort(Map.Entry.comparingByValue());
        
        for (int i=entryList.size()-1;i>=0;i--){
            k-=entryList.get(i).getValue();
            answer++;
            if (k <= 0) {
                break;
            }
            
        }
        return answer;
    }
}
```

