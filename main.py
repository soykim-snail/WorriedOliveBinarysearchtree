# 테크보이워니 - 코딩강좌
# 파이썬 기초: 변수, 티입, 조건문, 함수
# 인사하는 함수 만들기

# 이름과 나이를 받아라.
# 나이가 10살 미만이면 "안녕" 이라고 말해라
# 나이가 10살에서 20살 사이면 "안녕하세요" 라고 말해라
# 그 외에는 "안녕하십니까" 라고 말해라

def sayHello(name, age):
  if age < 10:
    print(f"{name}, 안녕")
  elif age >= 10 and age <= 20:
    print(f"{name}님, 안녕하세요.")
  else:
    print(f"{name}님, 안녕하십니까.")

sayHello("펭수", 10)

namedic = {
  "펭수": 10,
  "펭돌이" : 12,
  "동규" : 30
}

for name, age in namedic.items():
  sayHello(name, age)