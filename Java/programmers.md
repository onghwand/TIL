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

