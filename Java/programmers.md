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

