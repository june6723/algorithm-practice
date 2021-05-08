array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 7, 3]]
	

function solution(array, commands) {
  let answer = [];

  for(let i=0; i<commands.length; i++ ) {
    let start = commands[i][0]-1
    let end = commands[i][1]
    let target = commands[i][2] - 1
    let newArr = array.slice(start, end).sort((a,b)=> a-b)
    console.log(newArr)

    answer.push(newArr[target])
  }
  
  return answer;
}

console.log(solution(array, commands))