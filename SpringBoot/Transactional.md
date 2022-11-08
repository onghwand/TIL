## Transactional

### 🚨 Transaction이란?

데이터베이스에서 사용되는 용어로 tranaction은 데이터베이스 관리 시스템 또는 유사한 시스템에서 상태를 변화시키기 위해 수행하는 작업의 단위

<br>

### ✍️ transaction 특징

- **begin, commit**을 자동으로 수행해준다.
- 예외 발생 시 rollback 처리를 자동으로 수행해준다.
- Transaction은 4가지 성질을 가지고 있다: **원자성, 일관성, 격리성, 영속성**

<br>

### ✍️Transactional이란?

👉🏻 **@Transactional**은 클래스, 메소드, 인터페이스 위에 추가하여 사용하는 것으로, 해당 범위 내 메소드가 트랜잭션이 되도록 보장해준다. 다시 말해 메소드를 하나의 트랜잭션으로 간주하여 해당 메소드가 종료되기 전까지 어떠한 개입이나 다른 변화가 반영되지 않는 것을 말한다 . 이것을 **선언전 트랜잭션**이라고도 하는데, 직접 객체를 만들 필요 없이 선언만으로도 관리를 용이하게 해주기 때문이다.

<br>

### ✍️Transactional 사용 이유

 👉🏻 여러 SQL 쿼리를 처리할 때 그 중 하나가 오류난 경우 그 전에 실행되었던 SQL 쿼리들이 롤백이 되어야 데이터 베이스에 반영이 되지 않는다. 따라서 Transactional 어노테이션을 사용하면, 비즈니스 로직에서 데이터베이스로 SQL 쿼리 처리 과정 중 에러가 발생하면 트랜잭션이 롤백된다.

<br>

### ✍️이번에 사용한 부분

👉🏻 회원이 사용한 아이템 리스트를 받아서 순회하며 DB를 갱신하는 로직이다. 갱신 도중에 아이템의 개수가 0보다 작아지거나 없는 아이템인 경우 ERROR를 발생시킨다.

Transactional을 사용하지 않는다면 ERROR가 발생해도 그 전까지의 SQL 쿼리가 DB에 반영된다. 해당 상황을 방지하기 위해 Tranactional을 사용했고 중간에 ERROR가 발생하면 그 전의 쿼리들도 반영되지 않는다.

```java
	@Override
    @Transactional
    public void updateUserItemList(int userId, List<Integer> itemList) {
        /**
         * @Method Name : updateUserItemList
         * @Method 설명 : 회원 아이템 리스트를 수정한다.
         */

        HashMap<Integer,Integer> userItemMap = new HashMap<>();

        for (int i=0; i<itemList.size();i++) {
            int item = itemList.get(i);
            userItemMap.put(item, userItemMap.containsKey(item) ? userItemMap.get(item) + 1 : 1);
        }

        userItemMap.forEach((itemId, count) -> {
            UserItemBox userItemBox = userItemBoxRepository.findByUser_UserIdAndItem_ItemId(userId,itemId)
                    .orElseThrow(() -> new CustomException(ErrorCode.NOT_FOUND_USER_ITEM_INFO));

            // 변경된 개수가 0보다 작으면 오류
            int updatedCount = userItemBox.getCount() - count;
            if (updatedCount < 0) {
                throw new CustomException(ErrorCode.ITEM_COUNT_UNDER_ZERO_ERROR);
            }

            // count 갱신 후 저장
            userItemBox.changeCount(updatedCount);
            userItemBoxRepository.save(userItemBox);
        });
    }
```