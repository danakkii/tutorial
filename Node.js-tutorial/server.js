const express = require('express'); // 서버를 띄우기 위한 기본 셋팅
const app = express();

app.listen(8080, function(){ // listen(서버띄울 포트번호, 띄운 후 실행할 코드)
    console.log('listenging on 8080')
});

//누군가가 /pet으로 방문을 하면.. pet관련된 안내문을 띄워주자
// GET 요청을 처리하는 기계 제작하기

app.get('/pet', function(요청, 응답){
    응답.send('펫용품 쇼핑할 수 있는 사이트입니다.')
    console.log('펫용품 사이트')
});

app.get('/', function(요청, 응답){
    응답.sendFile(__dirname + '/index.html') // .sendFile(보낼파일경로)
});

