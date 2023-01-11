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

  - 종료조건에 해당하는 코드를 통해 반복문 종료
  - 조건이 참인 경우 들여쓰기 된 코드 블록이 실생됨
  - 코드 블록 실행 후 다시 조건식 검사하고 반복적 실행
  - 무한루프 하지 않도록 종료조건 반드시 필요

  ```python
  while <expression>:
    # Code bolock
  ```

- for문
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

# Python 3일차

## 함수(Function)

- 함수를 사용하는 이유 : Abstraction(추상) 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음. `재사용성, 가독성, 생산성`
- 특정한 기능을 하는 코드의 조각(묶음)
- 사용자 함수(Custom Function)

```python
def function_name
    # code block
    return returning_value
```

- 함수 기본 구조
  - 선언과 호출(define & call)
  - 입력(Input) : parameters
  - 범위(Scope)
  - 결과값(Output) : return

## 내장 함수

- print(\*objects, sep=' ', end='\n')

### 자주 사용하는 함수

- len(s) : 객체으 길이를 반환. 인자는 시퀀스 또는 컬렉션
- sum(iterable, start=0) : start 및 iterable(반복가능객체)의 항목을 왼쪽에서 오른쪽으로 합하고 합계를 돌려줌. 시작값은 문자열 될 수 없음
- max(iterable) : 가장 큰 항목이나 두 개 이상의 인자 중 가장 큰 것을 반환. 여러 항목이 최댓값이면 함수는 처음 만난 항목을 반환
- min(iterable) : 가장 작은 항목이나 두 개 이상의 인자 중 가장 작은 것을 반환. 여러 항목이 최솟값이면 함수는 처음 만난 항목을 반환

### 수학 관련 함수

- abs(x) : 절댓값 반환
- divmod(a, b) : 두 수를 받아 몫과 나머지 반환
- pow(base, exp, mod=None) : base의 exp 거듭제곱을 반환
- round(number, ndigit=None) : 반올림

### 논리 관련 함수

- all(iterable) : iterable의 모든 요소가 참이면(또는 iterable이 비어 있으면) True 반환
- any(iterable) : iterable의 요소 중 어느하나라도 참이면 True 반환. 비어 있으면 False 반환

### 기타 함수

- bin(x) : 정수를 '0b'접두사가 붙은 이진 문자열로 반환
- hex(x) : 정수를 '0x'접두사가 붙은 16진수 문자열로 반환
- oct(x) : 정수를 '0o'접두사가 붙은 8진수 문자열로 반환
- ord(c) : 문자 c에 대응되는 유니코드 정수로 반환
- chr(i) : 정수 i 에 대응 되는 유니코드 문자로 반환

## 함수 응용

- map(function, iterable)

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)를 적용하고, 그 결과를 map object로 반환

  ```python
  n , m = map(int, input().split())
  ```

# Python 4일차

## 컬렉션(Collections)

### 딕셔너리(Dictionary)

- 키-값(key-value)쌍으로 이뤄진 모음(collection) -키(key)
  - 불변 자료형만 가능(리스트, 딕셔너리 등은 불가능)
  - 값(values)
    - 어떠한 형태든 관계 없음
- 키와 값은 : 로 구분. 개별요소는 , 로 구분
- 변경 가능하며(mutable), 반복 가능함(iteable)
  - 딕셔너리는 반복하면 키가 반환 됨
- key와 value가 쌍으로 이뤄진 자료구조
  - key는 변경 불가능한 데이터(immutable)만 활용 가능
    -string, integer, gloat, boolean, tuple, range
  - value는 모든 값으로 설정 가능(list, dictionary 등)
- 딕셔너리에 키와 값의 쌍을 추가 가능
- 이미 해당 키가 있다면 기존 값이 변경
- 키 삭제 .pop()
- 키 없으면 KeyError
- 딕셔너리는 기본적으로 key를 순회, key를 통해 값을 활용
- 추가 메서드를 활용하여 순회 가능

```python
  - keys() : key로 구성
  - values() : value 로 구성
  - items(): (key, value)의 튜블로 구성된 결과

grades = {'Jeong': 80, 'Hwan': 100}
print(grades.keys())
print(grades.values())
print(grades.items())
```

## 모듈(Module)

- 모듈 : 다양한 기능을 하나의 파일로
- 패키지 : 다양한 기능을 하나의 폴더로
- 라이브러리 : 다양한 패키지를 하나의 묶음으로
- 이것을 관리하는 관리자(pip)

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지 포함

## 파이썬 표준 라이브러리

- [파이썬에 기본적으로 설치된 모듈과 내장함수](https://docs.python.org/ko/3/library/index.html)

### ramdom

- 숫자/수학 모듈 중 의사 난수 생성
  - 임의의 숫자 생성, 무작위 요서 선택, 무작위 비복원 추출
- random.randint(a, b)
  -a 이상 b 이하의 임의의 정수 N 반환
- random.choice(seq)
  - 비어있지 않은 시퀀스에서 임의의 요소 반환
  - seq가 비어있으면 IndexError
- random.shuffle(seq)
  - 시퀀스를 제자리에서 섞습니다.
- random.sample(population, k)
  - 무작위 비복원 추출한 결과인 k 길이의 리스트를 반환

### datetime

- 날짜와 시간을 조작하는 객체 제공
- 사용 가능한 데이터 타입
  - datetime.date, datetime.time, datetime.datetime, datetime,timedelta 등
- datetime.date(year, month, day)
  - 모든 인자가 필수. 인자는 특정 범위의 정수이어야 함.
  - 이 범위를 벗어나는 인자가 주어지면 ValueError 발생
- datetime.date.today()
  - 현재 지역의 날짜 반환
- datetime.datetime.today()
  - 현재 지역 datetime 반환. now()활용하면 타임존 설정

### os

- OS(운영체제)를 조작하기위한 인터페이스 제공
- os.listdir(path=',')
  - path(경로)에 의해 주어진 디렉터리에 있는 항목들의 이름을 담고 있는 리스트를 반환
  - 리스트는 임의의 순서로 나열되며, 특수 항목은 포함하지 않음
- os.mkdir(path)
  - path라는 디렉터리 만듦
- os.chdir(path)
  - path를 변경

## 파이썬 패키지

- 파이썬 패키지 관리자(pip)
  - Pypi(Python package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지관리 시스템
- 패키지 관리자(pip) 명령어
  - 패키지 설치
    - 최신 버전/특정 버전/최소 버전을 명시하여 설치 가능
    - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
  ```bash
  $ pip install SomePackage
  $ pip install SomePackage==1.0.5
  $ pip install 'SomePackage>=1.0.4'
  ```
  - 패키지 삭제
    - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌
  ```
  $ pip uninstall SomePackage
  ```
  - 패키지 목록 및 특정 패키지 정보
  ```
  $ pip list
  ```

## 에러/예외 처리(Error/Exceptin Handling)

### 디버깅

- 제어가 되는시점 조건/반복, 함수
- 값이 변경되는 시점
- branches
  - 모든 조건이 원하는대로 동작하는지
- for loops
  - 반복문에 진입한는지, 원하는 횟수만큼 실행되는지
- while loops
  - for loops와 동일, 종료조건이 제대로 동작하는지
- function

  - 함수 호출시, 함수 파라미터, 함수 결과

- print 함수 활용
- 개발환경(text edito, IDE)등에서 제공하는 기능 활용
- Python tutor 활용(단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

### 에러메시지

- 에러메시지 발생하는 경우 : 해당 위치 찾아 해결
- 로직에러가 발생하는 경우
  - 명시적 에러 메시지 없이 예상과 다른 결과가 나온 경우

### 에러와 예외

- 문법에러(Suntax Error)
- 예외(Exeption)
  - 실행 중 프로그램 실행을 멈춤
  - 실행 중 감지되는 에러를 예외(Exception)라고 부름
  - 여러 타입으로 나타남, 타입이 메시지의 일부로 출력 됨
  - 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
  - 사용자 정의 예외를 만들어 관리할 수 있음

### 예외처리

- try문(statement)/ ecept절(clause)을 이용하여 예외 처리 할 수 있음
- try문
  - 오류가 발생할 가능성 있는 코드를 실행
  - 예외가 발생되지 않으면, exept 없이 실행 종료
- ecept문
  - 예외가 발생하면, except절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
- 작성방법

```python
try:
  <try 명령문>
except 예외그룹-1 as 변수-1 :
  <예외처리 명령문 1>
except 예외 그룹-2 as 변수-2 :
  <예외처리 명령문 2>
finally:#선택사항
  <finally명령문>
```

- try : 코드를 실행
- except : try문에서 예외가 발생시 실행
- else : try문에서 예외가 발생하지 않으면 실행
- finally : 예외 발생 여부와 관계없이 항상 실행

### 예외 발생시키기

- raise를 통해 예외를 강제로 발생

```
raise <표현식>(메시지)
```

# Python 5일차

## 파일 입출력

### 파일 입력

- open(file, mode='r', encoding=None)
  - file : 파일명
  - mode : 텍스트 모드
  - encoding : 인코딩 방식(일반적으로 utf-8 활용)
  - 'r' : open for reading(default)
  - 'w' : open for writing, truncating th file first(덮어쓰기)
  - 'a' : open for writing, appending to th end of file if it exists

### 파일 활용

- 파일 객체 활용

```python
f = open('file', 'w')
f.closed
```

- with 키워드 활용

```python
with open('file') as f:
    read_data = f.read()
```

- with 키워드 사용하지 않으면, 'f.close()'를 반드시 호출하여 종료시켜야 오류가 발생하지 않음. 따라서 일반적으로 with 키워드를 활용하여 작성

### JSON

- JSON은 자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용
- 문자 기반(텍스트) 데이터포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능함
  - 텍스트를 언어별 데이터 타입으로 변환시키거나
  - 언어별 데이터 타입을 적절하게 텍스트로 변환

### JSON 파일의 활용

- 객체(리스트, 딕셔너리 등)를 JSON으로 변환

```python
import json
x = [1, 'simple', 'list']
json.dumps(x)
# [1, "simple", "list"]
```

- JSON을 객체(리스트, 딕셔너리 등)로 변환

```python
x = json.load(f)
```

### pprint

- 임의의 파이썬 데이터 구조를 예쁘게(정렬해서) 인쇄 할 수 있는 기능 제공

```python
from pprint import pprint
pprint()
```

# Python 6일차

## 튜플(Tuple)

- 불변한 값들의 나열(`값 변경 불가능`): List와 차이
- 순서 O 서로 다른 타입의 요소를 가질 수 있음
- 변경 불가(immutable), 반복 가능(iterable)
- () 형태이며, 요소는 콤마(,)로 구분
- 직접 만들어서 활용보다는 일반적으로 파이썬 내부에서 활용 ex) .items나 divmod

## 세트(Set)

- 유일한 값들의 모음(collection)
- 순서가 없고 중복된 값이 없음(특정 값 접근 불가)
- 변경 가능(mutable), 반복 가능(iterable)
- ({})또는 set()로 생성
- {} 딕셔너리는 키와 밸류의 합이고 세트는 그냥 값들의 합
- .add(): 값 추가
- .remove(): 값 삭제
- 중복 값을 쉽게 제거 가능
- 순서대로 출력하라고 하면 set 말고 반복문 써야 함. 순서가 다시 정렬되기 때문.

## 데이터 타입과 메서드

### 메서드(methods)

- 타입.`메서드`()
- 객체에서 실행되는 함수(?)
- 메서드 중 어떠한 것은 오류를 발생시키고 어떠한 것은 특정 값을 반환

### 문자열 메서드

- 문자열 탐색/검증

![image](https://user-images.githubusercontent.com/110805149/211324811-7700d2be-b6a5-434b-9542-db89ce5854a3.png)

- 문자열 변경

![image](https://user-images.githubusercontent.com/110805149/211325129-145a72a3-bebb-4a10-95aa-5bc05e550f58.png)

### 리스트 메서드

![image](https://user-images.githubusercontent.com/110805149/211325599-d78f9462-9eb4-4080-9a05-ab4d3e8d5c09.png)

- .remove : 값을 기준으로 삭제
- .pop : index 기준으로 삭제
- .extend : 리스트 + 리스트
- .sort 쓰면 원본 변경, 메서드는 원본 변경(.reverse 동일)
- sorted 는 함수라서 원본 그대로
- 어떠한 객체, 타입이 어떠한 메서드를 조작하는지 알고 써야 함

### 세트 메서드

![image](https://user-images.githubusercontent.com/110805149/211325796-1ac728be-1577-4e21-bc6b-e9de079de996.png)

- pop은 랜덤하게 항목을 반환: set는 인덱스가 없기 때문

### 딕셔너리 메서드

![image](https://user-images.githubusercontent.com/110805149/211326098-a23d21a1-fc64-451b-adf5-8691c15cee06.png)

- dict['k'] 키가 없으면 KeyError
- get(k) 키가 없으면 None 나옴
- get(k, 0) 하면 없으면 None 말고 0 나옴

## 간단 정리

- 숫자형
- Boolean
- None

### 시퀀스

- string : 문자의 나열 반복 O 변경 X
- list : 순서 O 반복 O 변경 O
- tuple : 순서 O 반복 O 변경 X
- range : 숫자의 나열 반복 O 변경 X

### 컬렉션

- set : 유일한 값들의 모음. 순서 X 반복 O 변경 O
- dictionary : 키-값들의 모음. 순서 X 반복 O 변경 O

### 참고

- for 문 끝까지 돌면 for-else로확인 가능!!
- 기술 관련 뉴스나 자료 볼 수 있는 곳
  - [GeekNews](https://news.hada.io/)
  - [요즘it](https://yozm.wishket.com/magazine/list/develop/)
  - 커리어리
  - 퍼블리

# Python 7일차

## 사용자 정의 함수

![image](https://user-images.githubusercontent.com/110805149/211582037-bde5d93a-6e37-4853-b93b-fdce606a13b6.png)

- 함수 정의 할 때 가장 중요한 것
  입력, 출력, 타입!!

```python
def foo(): # foo는 홍길동 같은 것이라는 설이 있다.
    retrun True

foo()
```

## 함수의 결과값(Output)

- 함수는 반드시 하나만 리턴
- 리턴과 동시에 실행 종료
- 명시적인 return이 없는 경우 : None
- 여러 값을 return 하는 경우 : tuple

## 함수의 입력(Input)

- Parameter : 함수를 실행할 때 내부에서 사용되는 식별자
- Argument : 함수를 호출 할 때, 넣어주는 값

```python
def foo(ham): # han : parameter
    retrun True

foo('spam') # 'spam' : argument
```

### Argument란

- 함수 호출 시 parameter를 통해 전달되는 값
- 필수 Argument : 반드시 전달되어야 하는 것
- 선택 Argument : 값을 전달하지 않아도 되는 경우 기본 값이 전달

#### positional argument : 기본적으로 위치에 따라 전달

```python
def add(x, y):
    return x + y

add(2,3)
```

#### keyword arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- keyword argument 다음에 positional argument 활용 안됨

```python
def add(x, y):
    return x + y

add(x = 2, y = 3)
add(2, y = 5)
```

### Default Arguments Values

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않아도 됨

```python
def add(x, y = 0):
    return x + y

add(2) # 2 + 0
```

- ex. print(\*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

### 정해지지 않은 개수의 arguments

- 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
- Argument 들은 튜플로 묶여 처리, parameter에 \*를 붙여 표현
- print함수는 오브젝트에 \*이붙어서 입력이 여러 개이더라도 나옴

```python
def add(*args):
    for arg in args:
      print(arg)

add(2)
add(2, 3, 4, 5) # 둘다 가능
```

### 정해지지 않은 개수의 keyword arguments

- 함수가 임의의 개수 Argument를 keyword Argument로 호출될 수 있도록 지정
- Argument들은 딕셔너리로 묶여 처리, parameter에 \*\* 붙여 표현

```python
def family(**kwargs):
    for key, value in kwargs.items(): #교재내용에 items() 추가
      print(key, ':', value)

family(father='John', mother='Jane', me='John Jr.')
```

### 함수의 scope

- LEGB

```python
# Built-in

# Global

def foo()
    # Enclosing Function Local
    def foo():
        # Local
```

- 함수 내부에서 글로벌 변수 변경

```python
a = 5
def boo():
    global a  # global scope의 a를 바꿔줌
    a = 3
    print(a)
```

## 참고

- utf-8 UTF-8 UTF8 다 되는 건가요?
  - UTF-8이 표준이라고 한다.(나머지는 경우에 따라)

# Python 8일차

- 부득이하게 교재를 옮겨 적음.. 이해 부족

## 사용자 정의 클래스

- 학습목표

  - 절차지향프로그래밍과 객체지향프로그래밍의 차이를 설명할 수 있다.
  - 클래스와 인스턴스의 차이를 비교하고 설명할 수 있다.
  - 클래스를 직접 정의하고 인스턴스를 생성할 수 있다.
  - 인스턴스 속성을 활용하고 메서드를 조작할 수 있다.

- 객체는 특정 타입의 인스턴스 이다.

### 객체

- 객체의 특징

  - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  - 속성(atribute) : 어떤 상태(데이터)를 가지는가?
  - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

- 객체지향 프로그래밍이란? -프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

- 절차 지향: 데이터와 함수로 인한 변화
- 객체 지향: 데이터와 기능(메소드)분리, 추상화된 구조(인터페이스)

![image](https://user-images.githubusercontent.com/110805149/211846060-76488d1e-4f69-4f0e-890b-110efebf02eb.png)

- 사각형 - 클래스(class)
- 각 사각형 - 인스턴스(instance)
- 사각형의 정보 - 속성(attribute)
- 사각형의 행동/기능 - 메소드(method)

## 클래스와 인스턴스

- 객체의 틀(클래스)를 가지고, 객체(인스턴스)를 생성한다.
- 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스
- 클래스: 객체들의 분류
- 인스턴스 : 하나하나의 실체/예
- 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 메소드 : 특정 데이터 타입/ 클래스의 객체에 공통적으로 적용 가능한 행위(함수)

- 인스턴스 변수 : 인스턴스가 개인적으로 가지고 있는 속성
- 생성자 메소드에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instace>.<name>으로 접근 및 할당

- 인스턴스 메소드
  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
  - 클래스 내부에 정의되는 메소드의 기본
  - 호출시, 첫번째 인자로 인스턴드 자기자신(self)이 전달됨
- self

  - 인스턴스 자기자신
  - 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫번째 인자로 정의
    - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

- 생성자(constructor) 메소드

  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - **init** 메소드 자동 호출

- 소멸자(destructor) 메소드 -인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

- 매직 메소드
  - Double underscore(\_\_)가 있는 메소드는 특수한 동작을 위해 만들어짐. 스페셜 메소드 혹은 매직 메소드
  - 특정 상황에 자동으로 불리는 메소드
  - **str** : 해당 객체의 출력 형태를 지정
  - **gt**: 부등호 연산자(>, greater than)

### 참고

- 클래스는 객체들의 타입..
- 클래스 내부의 함수는 모두다 메서드
- 참고사항은 아니지만.. 오늘 배운 클래스와 인스턴스는 추가 학습이 필요
