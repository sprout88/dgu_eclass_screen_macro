# dgu_eclass_screen_macro
동국대학교 이클래스 30초 안에 누르기를 수행하는 이미지 탐색-클릭 매크로입니다.

처음에는 브라우저의 dev console 로 작동하게 하려고 했으나, (document 객체 이용) 실패
대안으로 openCV 와 pyautogui 를 이용하여 1초에 한번씩 화면을 읽어 이미지를 찾으면 클릭합니다.
클릭하는 곳이 어디인지, 이미지 인식이 잘되는지, 사용자가 확인할 수 있도록 win32 API 를 이용하여 빨간색 가이드를 화면에 그리게 해서 사용성을 증대시켰습니다.
