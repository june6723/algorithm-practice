places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

function solution(places) {
  var answer = [];
  let length = 5
  for(let i=0; i<length; i++) {
      let waitingRoom = places[i]
      let people = []
      for(let r in waitingRoom) {
          for(let c in waitingRoom[r]) {
              if(waitingRoom[r][c]==="P") people.push([parseInt(r),parseInt(c)])
          }
      }
      // console.log(waitingRoom, people)
      if(people.length===0) {
        console.log('here')
        answer.push(0)
      }
        else{
            answer.push(check(waitingRoom,people))
        }
  }
  function check(wR,p) {
    // console.log(wR)
      while(p.length>0) {
          for(let i=1; i<p.length;i++) {
              let me = p[0]
              let other = p[i]
              // console.log(other)
              let rd = Math.abs(me[0]-other[0])
              let cd = Math.abs(me[1]-other[1])
              const md = rd+cd
              
              if(md===1) {
                  return 0
              } else if(md===2) {
                  if(rd === 2) {
                      if(wR[(me[0]+other[0])/2][me[1]] === 'O') return 0
                  } else if(cd === 2) {
                      if(wR[me[0]][(me[1]+other[1])/2] === 'O') return 0
                  } else{
                      if(wR[other[0]][me[1]] === 'O') return 0
                      if(wR[me[0]][other[1]] === 'O') return 0
                  }
              } 
          }
          p.shift()
      }
      return 1
  }
      
  return answer;
}

console.log(solution(places))