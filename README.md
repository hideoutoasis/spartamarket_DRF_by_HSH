# spartamarket_DRF_by_HSH
AI 6기 장고 심화주차 개인과제

<스파르타 마켓 소개><br/>
스파르타 마켓은 중고거래 서비스를 지원하는 웹페이지입니다. 누구나 회원가입만 하면 서비스를 이용할 수 있으며, 회원이 아닌 유저는 이용이 제한됩니다.
저번 과제 때와 비슷한 기능을 가진 웹페이지이며 이번에는 백엔드 기능개발에 완전히 초점이 맞춰져 있습니다.<br/><br/>

<구현된 기능 소개><br/>
스파르타 마켓은 기본적인 게시판의 형태를 가지는 플랫폼입니다.
그러므로 게시판의 기능인 CRUD 기능이 구현되어 있으며, 회원만 이용할 수 있으므로 user기능도 구현되어 있습니다.
모든 기능이 DRF에 의해 작성되어 있으므로 RESTful한 페이지라고 볼 수 있습니다.<br/><br/>

<사용 방법><br/>
스파르타 마켓을 이용하기 위해서는 일단 회원가입을 해야 합니다. 회원가입은 누구나 할 수 있으며 지연없이 바로 가입한 후 로그인, 로그아웃할 수 있습니다.
회원가입 이후에는 팔고자 하는 물건에 대한 글쓰기, 글 수정, 글 삭제, 글 조회를 할 수 있습니다.
물건에 대한 정보가 게시된 게시판에서는 물건에 대한 상세페이지를 조회할 수 있습니다.
사용자의 정보가 담긴 프로필 페이지에서는 사용자의 이름, 가입일자, 생일, 닉네임 등을 확인할 수 있습니다.<br/><br/>

<제작자><br/>
이 제품의 제작자는 저 한 명입니다. 두 번째 장고 프로젝트입니다.
저번보다 많은 것을 구현해보고 싶습니다.<br/><br/>

<프로젝트 ERD><br/>
초기 ERD입니다.<br/>
추가기능을 만약 넣게 되면 변경될 수 있습니다.
![spartamarket_DRF ERD](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/caa55031-2cdb-4d49-bb5c-0f0e99e8a803)
<br/><br/>


<기능구현 검증><br/>
![회원가입 기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/0b2f7d7a-84cc-4aed-9982-1ce740e56fa0)
회원가입 기능입니다.<br/>
필수 입력값을 전부 채워야 사용자를 생성할 수 있습니다. 비밀번호는 입력시 해싱되며, 포스트맨에서는 안보이지만 웹환경에서 보면 생일날짜는 DateField를 이용해서 받기 때문에 달력에서 선택하여 쉽게 입력할 수 있습니다.<br/><br/>

![로그인 기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/84181302-d39a-438f-86f6-c2eaea34583c)
![로그인 실패시](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/e64f183f-6d7e-4c35-be7e-b72ae637e020)
로그인 기능입니다.<br/>
알맞은 username과 password를 입력해야 로그인이 승인되며, 로그인 실패시 에러메세지를 출력합니다. 로그인 성공시 적절한 토큰을 발급합니다.<br/><br/>

![프로필 조회기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/0aeb3a6d-75cc-47e3-a10b-42ece039a7ab)
프로필 조회기능입니다.<br/>
로그인 후 토큰을 발급받고 사용자의 username에 맞는 주소로 들어와야 조회할 수 있습니다.<br/><br/>

![상품목록 조회기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/44c4f9fc-032b-4a94-a1aa-c2c4352e5f55)
상품 목록 조회기능입니다.<br/>
아무런 권한없이 접근할 수 있습니다.<br/><br/>

![상품 상세페이지 조회기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/386a9be5-a0ba-4a7d-a8ce-3ea564f65b87)
상품 상세페이지 조회기능입니다.<br/>
유효한 토큰을 가지고 있어야 접근할 수 있습니다.<br/><br/>

![상품등록 기능 토큰입력](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/857848dd-02bb-4c22-8cad-409ae00c367d)
![상품등록 기능 상품등록](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/f994c984-117b-471e-adba-50e110be452f)
상품 등록기능입니다.<br/>
마찬가지로 토큰이 있어야 접근할 수 있습니다.<br/>
이미지를 첨부할 수 있습니다. 첨부 안해도 글을 작성할 수 있게 만들어두었습니다.<br/><br/>

![상품 수정기능 토큰입력](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/c92cb262-0fbb-441d-9944-fce3509d1c26)
![상품 수정기능 상품수정](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/db5fe626-05ec-4161-aedd-570191705800)
상품 수정기능입니다.<br/>
등록한 상품을 수정할 수 있는데, 로그인하여 토큰을 발급받은 상태여야만 접근가능하고<br/>
![상품 수정 시 작성자 검증](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/5aef1753-5e25-4ef7-aaca-efa152ce1b28)
상품을 작성한 유저만 자신의 글을 수정할 수 있습니다.<br/>
이때 검증은 user 모델의 기본키를 product 모델에서 외래키로 받아와서 참조하여 작성자id author와 user id가 같은지 확인합니다.<br/>
<br/>

![상품 삭제기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/6b45af92-461d-4a88-b22a-f1fd04fab44b)
![상품삭제 확인](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/66ede019-8d1b-422f-be2f-43176ab19dbb)
상품 삭제기능입니다.<br/>
등록한 상품을 삭제할 수 있으며, 로그인 하여 토큰을 발급받은 상태에서 접근할 수 있고 수정과 마찬가지로 작성자와 요청자의 동일성을 검증합니다.
로직은 수정과 같습니다.<br/><br/>
![상품 삭제 시 작성자 검증](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/0e37413a-57e2-4a7d-a359-284b132a18c7)<br/><br/><br/>

<선택기능 구현>
페이지네이션 및 필터링, 정렬 기능을 구현했습니다.<br/>
상품 목록조회 시 페이지를 구분하여 나눠지도록 페이지네이션 구현했고, 제목과 내용으로 글을 찾기, 제목과 작성일자로 글 정렬하기 기능이 추가되었습니다.<br/>
![페이지네이션 필터링 기능](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/68a9b181-610b-4357-9003-8592297d3434)<br/>
키워드에 맞는 글이 없으면 null이 뜨고<br/>
![페이지네이션 필터링 기능 제목으로 찾기](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/49f4e312-f9f9-4d17-a1ad-0eca71501274)<br/>
![페이지네이션 필터링 기능 내용으로 찾기](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/8875cd59-103c-4777-afae-445a5825169b)<br/>
키워드에 맞는 글이 있다면 찾아낼 수 있습니다.<br/><br/>
![페이지네이션 필터링 정렬하기](https://github.com/hideoutoasis/spartamarket_DRF_by_HSH/assets/122522460/ff02b2be-bdf0-4787-a221-c8fbf4ceb6d6)<br/>
작성일자나 제목 순으로 정렬할 수도 있습니다.
















