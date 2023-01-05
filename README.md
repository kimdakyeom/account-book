# 가계부 API
## 개요
사용자의 소비내역을 기록/관리하는 가계부를 제공한다.
## DDL 파일 다운로드

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

#### 세부 내역 단축 URL
#### URL
> POST /books/<<int:pk>>/shortUrl

#### Response
**meta**
|Name|Type|Description|
|----|----|----|
|long_url|String|현재 url|
|short_url|String|단축된 url|