const targetNode = document.querySelector('body'); // 검색 대상 요소
const config = { childList: true, subtree: true }; // 감시할 변경 사항
const callback = function(mutationsList, observer) {
  for (const mutation of mutationsList) {
    if (mutation.type === 'childList') { // 자식 요소 변경 감지
        console.log("자식요소 변경 감지됨...")
        const popupButton = document.querySelector('body > form > div > div.footer > ul > li > a');
        if (popupButton) {
            console.log("클릭 요구 메세지 발견!")
            popupButton.click();
            console.log("클릭 요구 메세지 제거!")
            observer.disconnect(); // 콜백 함수 한 번 실행 후 감시 종료
      }
    }
  }
};
const observer = new MutationObserver(callback);
observer.observe(targetNode, config);
