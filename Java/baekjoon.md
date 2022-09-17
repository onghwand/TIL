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

### 구간합구하기4

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        st = new StringTokenizer(br.readLine());
        int arr[] = new int[n+1];
        arr[0] = 0;
        for (int i=1;i<n+1;i++) {
            arr[i] = arr[i-1] + Integer.parseInt(st.nextToken());
        }


        for (int j=0;j<m;j++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            System.out.println(arr[l]-arr[k-1]);
        }
    }
}

```

### 블랙잭

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int arr[] = new int[N];
        for (int i=0;i<N;i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int tmp = 0;
        int minV = M;
        int ans=0;
        for (int i=0;i<N;i++){
            for (int j=i+1;j<N;j++) {
                for (int k=j+1;k<N;k++){
                    tmp = arr[i]+arr[j]+arr[k];

                    if ( tmp <= M && Math.abs(M-tmp) < minV ) {
                        minV = Math.abs(M-tmp);
                        ans = tmp;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
```

