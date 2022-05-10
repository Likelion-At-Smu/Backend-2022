com_win = 0;
user_win = 0;

function game(user_give){
    //컴퓨터가 낼 결과를 int형태로 3가지 랜덤 결과를 생성한다. 0=가위 1=보 2=바위
    var com_give = parseInt(Math.random() * 3);

    //유저가 가위를 선택했을 때
    if(user_give==0){
        if(com_give==1){
            user_win++;
        }
        else if(com_give==2){
            com_win++;
        }
    }

    //유저가 보를 선택했을 떄
    else if(user_give==1){
        if(com_give==0){
            com_win++;
        }
        else if(com_give==2){
            user_win++;
        }
    }

    //유저가 바위를 선택했을 때
    else if(user_give==2){
        if(com_give==0){
            user_win++;
        }
        else if(com_give==1){
            com_win++;
        }
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
