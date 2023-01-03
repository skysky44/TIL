# Python 1일차

## 컴퓨터 프로그래밍 언어

- 컴퓨터(Computer): 조작(Caculation)+저장(Remember)
- 프로그래밍: 명령어의 모음(집합) ex.엑셀은 스프레드시트 조작하기위한 명령어 모음
- 언어 : 자신의 생각을 나타내고 전달하기 위해 사용하는 체계
- 선언전 지식(declarative knowledge): 사실에 대한 내용
- 명령적 지식(imperative knowledge): How to

## 파이썬(Python)의 특징

- 인터프리터 언어(Interpreter)

  - 소스코드를 `기계어로 변환하는 컴파일 과정 없이` 바로 실행 가능
    - 컴파일은 인간이 이해할 수 있는 언어로 작성된 소스 코드(고수준 언어 : C, C++, Java 등)를 CPU가 이해할 수 있는 언어(저수준 언어 : 기계어)로 번역(변환)하는 작업
  - 코드를 대화하듯 한 줄 입력하고 실행 후, 바로 확인 가능

- 객체 지향 프로그래밍(Object Oriented Programming)
  - 파이썬은 모두 `객체(Object)`로 구성되어 있다.
    - 객체는 어떠한 물건을 어려운 말로 표현한 것뿐. 박스에 무언가 담을 건데 그 담는 어떠한 것!.객체 ~(어떠한) 것 : 사물
- 변수
  - 메모리 어딘가에 저장되어있는 객체를 참조하기 위해 사용 되는 이름
    - 객체: 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
  - 동일 이름에 다른 객체를 언제든 할당할 수 있기 때문에 변수라고 불림
  - 할당 연산자(=)를 통해 할당

## 객체의 종류

- 수치형

  - 정수(Int)
  - 실수(Float)
    - 부동소수점: 실수를 컴퓨터가 표현하는 방법. 예상치 못한 결과 주의
      ```
      3.14 -3.02 == 0.12 # 참일까?
      # 0.12000000...0001 == 0.12 -> False
      ```
  - 불린형(Boolean type)
    - True/False(대문자로 써야됨)

- 연산자(Operator)

  - 산술 연산자 : +, =, \*, %(나머지), /(나눗셈) //(몫), \*\*(거듭제곱)
  - 비교 연산자 : <, <=, >, >=, ==(같음), !=(같지않음)
  - 논리 연산자 : and, or, Not

- 컨테이너

  - 여러 개의 값을 담을 수 있는 것(객체)
  - 컨테이너 분류 : 순서가 있는 데이터(Ordered) vs 순서가 없는 데이터(Unordered)
  - 시퀀스

    - 문자열

      - str 타입
      - ''나 "" 활용하여 표기
      - 여러줄 입력 삼중따옴표 '''문자열''' 또는 """문자열"""
      - \n : 줄바꿈, \t : 탭

    - 리스트 : 변경 가능한 값들의 나열
      - [] 또는 list() 통해 생성
      - 순서가 있는 시퀀스. 인덱스를 통해 접근
      - 값 추가 : .append()
      - 값 삭제 : .pop()
    - 튜플 : 변경 불가능한 값들의 나열
    - 레인지 : 숫자의 나열

  - 컬렉션/비시퀀스

    - 세트 : 유일한 값들의 모음
    - 딕셔너리 : 키 값들의 모음

- None
  - 값이 없음을 표현하기 위해 None 타입 존재

## 코드 작성 주의 사항

- 대소문자 구분
- 띄어쓰기, 문장부호 등 주의
- 들여쓰기 할 때는 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력
  - 혼용하면 안됨

## 주석

- 코드에 대한 설명
- 앞에 '#' 입력

## 사용자 입출력

- input([prompt])
  - `반환값은 항상 문자열의 형태`로 반환
- print()

## 참고 단축키

- clear : 터미널 지우기
- 한 줄 선택 : ctrl + L 또는 shift+ 화살표 아래
- 주석 처리 하기 : ctrl+/

# Python 2일차

## string Interpolation

- 문자열을 변수를 활용하여 만드는 법
- %-formatting(과거에 많이 씀)

```python
name = kim
score = 4.5
print('Hello, %s' % name)
print('내 성적은 %d' % score) # 4
print('내 성적은 %f' % score) # 4.500000
```

- f-stiring(현재 많이 씀)

```python
name = kim
score = 4.5
print(f'Hello, {name}! 성적은 {score}')
```

## 형 변환(Typecasting)

- 자료형 변환(Typecasting)
  - 파이썬에서 데이터 형태 서로 변환 가능
  - 암시적 형 변환(Implicit) : 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
    - bool
    - NUmeric type(int, float, complex)
    ```
    True + 3
    # 4
    3 + 5.0
    # 8.0
    ```
  - 명시적 현 변환(Explicit) : 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환 하는 경우
  - int : str(형식에 맞는 문자열만 가능), float -> int
  - float : str(형식에 맞는 문자열만 가능), int -> float
  - str : int, float, list, tuple, dict -> str
- 변수의 Type을 아는 것 중요

## 제어문(Control Statement)

- 파이썬은 기본적으로 위에서부터 아래로 순차적 명령 수행

## 조건문(Conditional Statement)

```python
if <expression>:
    # Run this Code block
else:
    # Run this Code block
```

- expression에 참/거짓에 대한 조건식
- 콜론(:) : 이것이 if 문이다를 나타냄
- 띄어쓰기 : 스페이스 4칸.. 약속(?)

- 복수 조건문

```python
if <expression>:
    # Run this Code block
elif <expression>:
    # Run this Code block
elif <expression>:
    # Run this Code block
else:
    # Run this Code block
```

- 중첩 조건문

```python
if <expression>:
    # Run this Code block
    if <expression>:
    # Run this Code block
else:
    # Run this Code block
```

- 레인지(Range)
  - 기본형 : range(start)
  - 범위지정 : range(start, stop)
  - 범위 및 스텝 지정 : range(start, stop, step)
  - 레인지는 숫자의 시퀀스를 나타내기 위해 사용

## 반복문(Loop Statement)

- while문
- fot문
  - for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함
  - 처음부터 끝까지 모두 순회. 별도의 종료조건 불필요
  - 순회가능한 객체 : 컨테이너형(string, tuple, list, range, set, dicionary)
- 반복제어 : break, continue, for-else
  - break : 반복문 종료
  - continue : continue 이후의 코드 블록은 수행하지 않고 다음 반복을 수행(다시 처음부터 수행)
  - for-else 끝까지 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음(break에 안걸리면 else문 실행)
  ```python
  for char in 'apple':
      if char == 'b':
        print('b!')
        break
  else:
      print('b가 없습니다.')
  ```

## 참고

- [파이썬튜터](https://pythontutor.com/) : 단계별 실행 과정을 볼 수 있음
