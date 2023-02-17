### :taco: 템플릿메소드 패턴, Template Method Pattern

> 여러 클래스에서 공통으로 사용하는 메서드를 템플릿화하여 상위 클래서에서 정의하고 하위 클래스마다 세부 동작 사항을 다르게 구현하는 패턴



> 코드 예시

```java
abstract class Pizza {
    protected void 반죽() { System.out.println("반죽"); }
    abstract void 토핑();
    protected void 굽기() { System.out.println("굽기"); }

    final void makePizza() {
        this.반죽();
        this.토핑();
        this.굽기();
    }

}

class PotatoPizza extends Pizza {
    @Override
    void 토핑() {
        System.out.println("감자");
    }
}

class TomatoPizza extends Pizza {

    @Override
    void 토핑() {
        System.out.println("토마토");
    }
}

public class Main {
    public static void main(String[] args) {
        Pizza potatoPizza = new PotatoPizza();
        potatoPizza.makePizza();

    }
}
```



> 장점

- 상위 추상클래스로 로직을 공통화하여 코드의 중복을 줄일 수 있다

> 단점

- 제공된 골격에 의해 유연성이 제한될 수 있다



#### :label: 참고

- https://gyoogle.dev/blog/design-pattern/Template%20Method%20Pattern.html
- https://inpa.tistory.com/entry/GOF-%F0%9F%92%A0-%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%A9%94%EC%86%8C%EB%93%9CTemplate-Method-%ED%8C%A8%ED%84%B4-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EB%B0%B0%EC%9B%8C%EB%B3%B4%EC%9E%90