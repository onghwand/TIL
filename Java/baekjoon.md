### 수 정렬하기

> Scanner 336ms

```java
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] =new int[N];

        for (int i=0;i<N;i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);

        for (int i=0;i<N;i++) {
            System.out.println(arr[i]);
        }
    }
}
```

> BufferedReader 176ms
>
> 확실히 빠르다

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int arr[] =new int[N];

        for (int i=0;i<N;i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        for (int i=0;i<N;i++) {
            System.out.println(arr[i]);
        }
    }
}
```



