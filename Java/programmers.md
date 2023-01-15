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
### 할인행사

```java
import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        for (int i=0;i<number.length;i++) {
            map.put(want[i],number[i]);
        }
        
        for (int i=0;i+10<=discount.length;i++) {
            Map<String, Integer> map1 = new HashMap<>();
            for (int j=i;j<i+10;j++) {
                map1.put(discount[j], map1.getOrDefault(discount[j],0)+1);
            }
            
            if (map1.equals(map)) {
                answer++;
            }
        }
        
        return answer;
    }
}
```

### 점 찍기

```java
import java.lang.*;
class Solution {
    public long solution(int k, int d) {
        long answer = d/k*2+1;
        
        for (int i=k;i<=d;i+=k) {
            // d가 1000000이면 int가 담을 수 없기 때문에 음수값으로 바뀜..
            // answer += Math.floor(Math.sqrt((d*d-i*i)))/k; 
            answer += (long) Math.sqrt(((long)d*d-(long)i*i))/k;
        }
        
        return answer;
    }
}
```

### 롤케이크 자르기

```java
import java.util.*;
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        if (topping.length == 1) {
            return 0;
        }
        
        Map<Integer, Integer> front = new HashMap<>();
        Map<Integer, Integer> back = new HashMap<>();
        for (int i=0;i<topping.length;i++) {
            front.put(topping[i], front.getOrDefault(topping[i],0)+1);
        }
        
        for (int i=topping.length-1;i>=0;i--) {
            if (front.get(topping[i]) > 1) { 
                front.put(topping[i], front.get(topping[i])-1);
            } else {
                front.remove(topping[i]);
            }
            
            back.put(topping[i], front.getOrDefault(topping[i],0)+1);
            
            if (front.keySet().size() == back.keySet().size()) {
                answer++;
            }
        }
        
        return answer;
    }
}
```

### 택배상자

```java
import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> tmp = new Stack<>();

        int idx = 0;
        for (int i=1;i<order.length+1;i++){
            while (tmp.size() > 0 && tmp.peek() == order[idx]) {
                answer++;
                idx++;
                tmp.pop();
            } 

            if (i == order[idx]) {
                answer++;
                idx++;
            } else {
                tmp.push(i);
            } 
        }


        while (tmp.size() > 0) {
            if (tmp.pop() != order[idx]) {
                break;
            } else {
                idx++;
                answer++;
            }
        }
        return answer;
    }
}
```

### 숫자 카드 나누기

```java
import java.util.*;
class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        int L = arrayA.length;
        int minA = arrayA[0]; int minB = arrayB[0];
        Set<Integer> set = new HashSet<>();
        for (int i=2;i<=minA;i++) {
            if (minA%i==0) set.add(i);
        }
        for (int i=2;i<=minB;i++) {
            if (minB%i==0) set.add(i);
        }
        
        List<Integer> list = new ArrayList<>(set);
        list.sort(Comparator.naturalOrder());
        
        for (int i=list.size()-1;i>=0;i--) {
            int cntA=0; 
            int cntB=0;
            
            for (int j=0;j<L;j++) {
                if (arrayA[j]%list.get(i) == 0) {
                    cntA++;
                }
                if (arrayB[j]%list.get(i) == 0) {
                    cntB++;
                }
            }
            
            if ((cntA==0 && cntB==L) || (cntA==L && cntB==0)) {
                answer = list.get(i);
                break;
            }
        }
        return answer;
    }
}
```

### 테이블 해시 함수

```java
import java.util.*;
class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        Arrays.sort(data, (o1,o2) -> {
            if (o1[col-1]==o2[col-1]) {
                return o2[0]-o1[0];
            } else {
                return o1[col-1]-o2[col-1];
            }
        });
        
        for (int i=row_begin;i<=row_end;i++) {
            int total = 0;
            for (int j=0;j<data[i-1].length;j++) {
                total += data[i-1][j]%i;
            }
            answer = answer ^ total;
        }
        
        return answer;
    }
}
```

### 우박수열 정적분

```java
import java.util.*;
class Solution {
    public double[] solution(int k, int[][] ranges) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0,k);
        int cnt = 1;
        while (k!=1) {
            if (k%2==1) {
                k = k*3+1;
            } else {
                k = k/2;
            }
            map.put(cnt, k);
            cnt++;
        }

        double[] areas = new double[cnt-1];
        for (int i=0;i<cnt-1;i++) {
            double area = (double)(map.get(i)+map.get(i+1))/2;
            areas[i] = area;
        }

        double[] answer = new double[ranges.length];
        for (int i=0;i<ranges.length;i++) {
            int start = ranges[i][0]; int end = cnt+ranges[i][1]-1;
            if (start > end) {
                answer[i] = -1;
            } else if (start == end) {
                answer[i] = 0;
            } else {
                double total = 0;
                for (int j=start;j<end;j++) {
                    total += areas[j];
                }
                answer[i] = total;
            }
        }

        return answer;
    }
}
```

