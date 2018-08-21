# S-School-Project-HandS

**7월 일정**
- 공유기 구매이후 라즈베리파이 ip 고정
- 스트리밍 테스트 및 추가 라즈베리파이 구매여부 결정
- 사용자용 장갑 설계(재질,색깔,모양 등)
         
**Leap**
- Windows에서 진행
- 비주얼라이저 끈 상태로 실행
1. 이전버전 sdk 다운 => 설치
https://developer.leapmotion.com/sdk/v2

2. Python27 bit확인
-> 32bit : LeapSDK/lib/x86 사용
-> 64bit : LeapSDK/lib/x64 사용

3. leap 폴더추가 : ~path/Python27/leap
- leap폴더에 아래 파일들 저장
	1) Leap(LeapSDK/lib에 존재)
	2) Leap.dll (LeapSDK/lib/x86 or x64 에 존재)
	3) Leap (LeapSDK/lib/x86 or x64 에 존재)
	4) LeapPython(LeapSDK/lib/x86 or x64 에 존재)
	5) Sample.py(LeapSDK/samples에 존재)
	6) leapimg.py(git에 존재 - 이미지처리)
- ~ .py 파일들 실행.

4. Sample.py 실행 
-안되면 못돌림...............
-cmd로 돌릴것.(python leap/Sample.py)
- 64bit으로 실행 안되면 32bit으로 

5. leapimg.py 실행

- leapmotion을 양손 중앙에 놓고 실행.

- 왼손 : forward, backward, break 조절
	-  손 편 상태로 특정 높이를 기준으로 forward, backward 구분
	- 주먹 쥐면 break
- 오른 손 : 방향조절(left+3~right+3)
	- 핸들 조절하듯 손 전체로 반원 그리면 됨.
	
-print값 : total_data 

cf.  방향 이상하면 코드 수정.

**실행 방법**
1. PuTTY로 라즈베리파이에 접속.
2. cd Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server 
3. sudo python main2.py
4. Leap.py 실행 

**How to start in Ubuntu**
1. Install Leap SDK.
2. $ sudo dpkg --install Leap-2.3.1+31549-x64.deb (64bit) or $ sudo dpkg --install Leap-2.3.1+31549-x86.deb (32bit)
3. Go to /usr/bin or /usr/sbin.
4. $ sudo leapd
5. $ python Sample.py or $ python leapimg.py
