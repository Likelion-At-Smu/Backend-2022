//컴퓨터가 이긴 횟수
var com_win = 0;
//사용자가 이긴 횟수
var user_win = 0;
//결과 텍스트
var res_text = new Array('WIN!!', "LOSE..", "DRAW");
//결과 값 0은 승리, 1은 패배, 2는 비김
var res = 0;

function game(user_give){
    //컴퓨터가 낼 결과를 int형태로 3가지 랜덤 결과를 생성한다. 0=가위 1=보 2=바위
    var com_give = parseInt(Math.random() * 3);

    //유저가 가위를 선택했을 때
    if(user_give==0){
        if(com_give==1){
           user_win++;
            res = 0;
        }
        else if(com_give==2){
            com_win++;
            res = 1;
        }
        else{
            res=2;
        }
    }

    //유저가 보를 선택했을 떄
    else if(user_give==1){
        if(com_give==0){
            com_win++;
            res = 1;
        }
        else if(com_give==2){
            user_win++;
            res = 0;
        }
        else{
            res=2;
        }
    }

    //유저가 바위를 선택했을 때
    else if(user_give==2){
        if(com_give==0){
            user_win++;
            res = 0;
        }
        else if(com_give==1){
            com_win++;
            res = 1;
        }
        else{
            res = 2;
        }
    }

    //결과 출력
    document.getElementById('result').innerHTML = res_text[res];
    //결과에 따라 텍스트의 색깔 변경
    if(res==0){
        document.getElementById('result').style.color = 'red';
    }
    else if(res==1){
        document.getElementById('result').style.color = 'blue';
    }
    else{
        document.getElementById('result').style.color = 'black';
    }

    //유저와 컴퓨터가 낸 결과를 이미지로 출력
    document.getElementById('user_give').src = user_give+'.png'
    document.getElementById('computer_give').src = com_give+'.png'

    //총 승리 횟수를 업데이트
    document.getElementById('user_win_cnt').innerHTML = 'YOU : ' +user_win;
    document.getElementById('com_win_cnt').innerHTML = 'COMPUTER : ' +com_win;
    console.log('컴퓨터'+com_give);
    console.log('유저'+user_give);
}
