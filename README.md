# 가계부 API
## 개요
사용자의 소비내역을 기록/관리하는 가계부를 제공한다.
## DDL 파일
- [DDL 파일](https://github.com/kimdakyeom/account-book/blob/master/account_db.ddl)

## 사용한 외부 라이브러리
- [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/)
  - 사용 목적 : JWT 토큰 기반 로그인/회원가입
- [pyshorteners](https://pyshorteners.readthedocs.io/en/latest/)
  - 사용 목적 : 단축 URL
## API 명세
### 회원가입
#### URL
> POST /accounts/registration/
#### Request
**Parameter**
|Name|Type|Description|
|----|----|----|
|email|String|이메일|
|password1|String|설정할 비밀번호|
|password2|String|설정할 비밀번호 확인|
#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|access_token|String|엑세스 토큰|
|refresh_token|String|리프레시 토큰|
|user|String|유저 정보|

### 로그인
#### URL
> POST /accounts/login/
#### Request
**Parameter**
|Name|Type|Description|
|----|----|----|
|email|String|이메일|
|password|String|비밀번호|

#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|access_token|String|엑세스 토큰|
|refresh_token|String|리프레시 토큰|
|user|String|유저 정보|

### 로그아웃
#### URL
> POST /accounts/logout

<hr>

### 가계부
### CURD
#### URL
> GET
> POST /books/
#### Request
**Parameter**
|Name|Type|Description|
|----|----|----|
|price|Int|금액|
|memo|String|관련 메모|

#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|id|Int|가계부 아이디|
|user|String|작성자|
|price|Int|금액|
|memo|String|관련 메모|
|note_at|Date|작성 날짜|

#### URL
> GET
> PUT
> DELETE /books/<<int:pk>>
#### Request
**Parameter**
|Name|Type|Description|
|----|----|----|
|price|Int|금액|
|memo|String|관련 메모|

#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|id|Int|가계부 아이디|
|user|String|작성자|
|price|Int|금액|
|memo|String|관련 메모|
|note_at|Date|작성 날짜|

#### 가계부 세부 내역 복제
#### URL
> POST /books/<<int:pk>>
#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|id|Int|가계부 아이디|
|user|String|작성자|
|price|Int|금액|
|memo|String|관련 메모|
|note_at|Date|작성 날짜|

- 가계부 리스트에서 복제, 세부 내역 페이지에서 이루어지는지에 따라 이후 행동도 달라져서 어떻게 설계할지 고민했습니다. 수정/삭제 또한 세부 내역 페이지에서 가능하도록 설계했기 때문에 복제도 세부 내역 페이지에서 가능하도록 했습니다.

#### 세부 내역 단축 URL
#### URL
> POST /books/<<int:pk>>/shortUrl

#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|long_url|String|현재 url|
|short_url|String|단축된 url|

- pyshorteners 라이브러리를 이용해서 tinyurl 서비스를 활용했습니다. 만료시간을 따로 설정하지 못해서 그 부분은 구현하지 못했습니다.

<hr>
- 로그인/회원가입 기능에 대한 테스트 케이스 작성을 완료했습니다.