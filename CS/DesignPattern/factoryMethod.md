### :factory: 팩토리 메소드 패턴, Factory Method

> 객체 생성을 Sub class에 맡기는 패턴



> 코드

```java
// Pizza
abstract class Pizza {
    String dow;
}

public class CheesePizza extends Pizza{
    public CheesePizza() {};

    @Override
    public String toString() {
        return "치자피즈";
    }
}

public class PotatoPizza extends Pizza{
    public PotatoPizza() {};

    @Override
    public String toString() {
        return "포테토피자";
    }
}

// Factory
public abstract class PizzaFactory {

    public Pizza newPizza() {
        Pizza pizza = createPizza();
        return pizza;
    }
    abstract Pizza createPizza();
}

public class CheesePizzaFactory extends PizzaFactory{
    @Override
    Pizza createPizza() {
        return new CheesePizza();
    }
}

public class PotatoPizzaFactory extends PizzaFactory{
    @Override
    Pizza createPizza() {
        return new PotatoPizza();
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        // 기존에 치즈피자 밖에 없음
        PizzaFactory pizzaFactory = new CheesePizzaFactory();
        Pizza pizza = pizzaFactory.createPizza();
        System.out.println(pizza); // 치자피즈

        // 신메뉴 포테이토가 나와도 기존 코드 형식을 수정하지 않으면서 확장 가능(OCP)
        PizzaFactory potatoPizzaFactory = new PotatoPizzaFactory();
        Pizza potatoPizza = potatoPizzaFactory.createPizza();
        System.out.println(potatoPizza); // 포테토피자
    }
}
```



> 장점

- OCP원칙을 지킬 수 있음

> 단점

- 클래스가 많아지고 코드량이 증가함

<br>

#### 참고

- https://gyoogle.dev/blog/design-pattern/Factory%20Method%20Pattern.html
- https://dev-youngjun.tistory.com/195
- https://bcp0109.tistory.com/367