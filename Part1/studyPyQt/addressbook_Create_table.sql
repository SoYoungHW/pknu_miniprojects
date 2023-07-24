-- MySQL용
CREATE TABLE addressbook (
  Idx int NOT NULL AUTO_INCREMENT COMMENT 'PK 자동증가',
  FullName varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '이름',
  PhoneNum varchar(20) NOT NULL COMMENT '전화(핸드폰)번호',
  Email varchar(120) DEFAULT NULL COMMENT '이메일 Null허용',
  Address varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '주소 Null허용',
  PRIMARY KEY (Idx)
) COMMENT='주소록 테이블';