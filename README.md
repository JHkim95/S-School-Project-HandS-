# S-School-Project-HandS

**9월 일정**
- 전시 판넬 제작
- 자동차 하드웨어(외관 및 LED) --> 선택사항  
(LED : 운행/정지를 녹색/적색과 같이 간단히 표시)
- 립모션 코드 실행하여 손동작 편리하게끔 최적화/수정  
- 전시회장 맵 및 장애물 제작 관련 회의  
  
**제스쳐 인식 방식**  
왼손(보자기)   : 수직 Depth를 이용하여 전진(립모션과 가까이), 후진(멀리)  

왼손(주먹)     : 정지  

오른손(보자기) : 평행 좌우이동으로 자동차의 다섯가지 조향제어(좌로 2단계,전진, 우로 2단계)  
  
**우분투 작동방식 최종**
1. 립모션 연결, LeapSDK 2.3.1 다운로드하기
  
2. cmd(1)   
  -> cd /usr/bin  
  -> sudo leapd
	    
3. cmd(2)   
  -> putty or ssh 로 라즈베리파이 접속    
  -> cd Sschool/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server    
  -> python Smain.py (모터 제어 코드)
	    
4. cmd(3)   
  -> cd LeapDeveloperKit_2.3.1+31549_linux/LeapSDK/samples  
  -> samples 디렉토리에 check.py(제스쳐 인식코드) 넣기    
  -> python check.py  
    
**웹**
(http://ssss0902.pythonanywhere.com/ 파일이랑은 다른 파일임. 좀더 간단한게 확인가능.)
(leapmotion 연결 )
1. s-school web 다운
2. 서브라임으로 testleap.html 실행 
3. ctrl+B 
         
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
2. cd Sschool/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server 
3. sudo python main2.py
4. Leap.py 실행 

**How to start in Ubuntu**
1. Install Leap SDK.
2. $ sudo dpkg --install Leap-2.3.1+31549-x64.deb (64bit) or $ sudo dpkg --install Leap-2.3.1+31549-x86.deb (32bit)
3. Go to /usr/bin or /usr/sbin.
4. $ sudo leapd
5. $ python Sample.py or $ python leapimg.py

>>![example2](https://user-images.githubusercontent.com/36954727/44376796-04f7d280-a535-11e8-8414-cfaa66760738.jpeg)
>>Success!


