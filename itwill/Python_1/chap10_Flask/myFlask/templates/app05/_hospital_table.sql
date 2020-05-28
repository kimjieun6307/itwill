-- hostpital_table.sql

-- 1. 의사 테이블 
create table doctors(  
doc_id int(10) primary key,
major_treat varchar(25) not null, 
doc_name varchar(20) not null,
doc_gen char(1) not null,
doc_phone varchar(15) not null,
doc_email varchar(20) not null,
doc_position varchar(20) not null
);

insert into DOCTORS values(980312, '소아과', '이태정', 'M', '010-333-1330', 'itj@naver.com','과장');
insert into DOCTORS values(000601, '내과', '안성기', 'M', '010-444-1440', 'ask@naver.com','과장');
insert into DOCTORS values(001208, '외과', '김민종', 'M', '010-222-1220', 'kmj@naver.com','과장');
insert into DOCTORS values(020403, '피부과', '이태서', 'M', '010-111-1110', 'lts@naver.com','전문의');
insert into DOCTORS values(050900, '소아과', '김연아', 'F', '010-555-1550', 'itj@naver.com','전문의');

select * from DOCTORS;


-- 2. 간호사 테이블 
create table nurses(
nur_id int primary key,
major_job varchar(25) not null,
nur_name varchar(20) not null,
nur_gen char(1) not null,
nur_phone varchar(15) null,
nur_email varchar(50) unique,
nur_position varchar(20) not null
);

insert into nurses values(050302, '소아과', '김은영', 'F', '010-555-8751', 'kim@naver.com', '수간호사');
insert into nurses values(050021, '내과', '윤성애', 'F', '010-444-8751', 'ysa@naver.com', '수간호사');
insert into nurses values(040089, '방사선과', '신지원', 'M', '010-666-8661', 'sjw@naver.com', '주임');
insert into nurses values(100356, '피부과', '유정화', 'F', '010-333-7551', 'yjw@naver.com', '간호사');
insert into nurses values(102101, '외과', '리히나', 'F', '010-222-1234', 'nnn@naver.com', '간호사');

select * from nurses;

-- 3. 환자 테이블 : 2개 외래키 지정 
CREATE table patients(
pat_id int primary key,
nur_id int not null,
doc_id int not null,
pat_name varchar(20) not null,
pat_gen char(1) not null,
pat_jumin varchar(14) not null,
pat_addr varchar(100) not null,
pat_phone varchar(15) null,
pat_email varchar(50) unique,
pat_job varchar(20) not null,
foreign key(nur_id) references nurses(nur_id),
foreign key(doc_id) references doctors(doc_id)
);

insert into patients values(1234, 050021, 000601, '안상건', 'M', 232345, '서울', '010-555-4578', 'ask@naver.com', '회사원');
insert into patients values(3456, 100356, 020403, '김성룡', 'M', 543545, '서울', '010-333-7842', 'ksr@naver.com', '자영업');
insert into patients values(2541, 050021, 000601, '이종진', 'M', 433424, '부산', '010-222-2278', 'lss@naver.com', '회사원');
insert into patients values(4522, 102101, 001208, '이진희', 'F', 119768, '서울', '010-888-4578', 'ljh@naver.com', '교수');
insert into patients values(9785, 050302, 050900, '오나미', 'F', 987645, '서울', '010-555-4578', 'onm@naver.com', '학생');

select * from patients;

-- 4. 진료 테이블 
create table treatments(
treat_id int primary key,
pat_id int not null,
doc_id int not null,
treat_contents varchar(1000) not null,
tread_date date null, 
foreign key(pat_id) references patients(pat_id),
foreign key(doc_id) references doctors(doc_id)
);

insert into treatments values(130516023, 1234, 000601, '감기,몸살', '2013-05-16');
insert into treatments values(134121420, 3456, 020403, '피부 트러블 치료', '2013-06-28');
insert into treatments values(131205056, 2541, 000601, '배탈, 설사', '2013-12-10');
insert into treatments values(131224012, 4522, 001208, '위궤양', '2014-05-10');
insert into treatments values(140109026, 9785, 050900, '중이염', '2015-03-12');


SELECT * FROM treatments;

# AUTO COMMIT