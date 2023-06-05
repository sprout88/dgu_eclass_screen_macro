const INTERVAL=1000
setInterval(function() {
  var popupButton = document.querySelector('body > form > div > div.footer > ul > li > a');
  if (popupButton) {
    console.log("클릭 요구 메세지 발견!")
    popupButton.click();
    console.log("클릭 요구 메세지 제거!")
  }else{
    console.log(`클릭 요구 메세지가 발견되지 않았습니다. interval : ${INTERVAL}`)
  }
}, INTERVAL);


var popupButton = document.querySelector('body > form > div > div.footer > ul > li > a');
popupButton.click();