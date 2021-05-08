numbers	= [6, 10, 2]	
numbers2	= [3, 30, 34, 5, 9,667,66]

function solution(numbers) {
  let answer = '';
  let list = numbers
  
  answer = list.map((num)=> num.toString()).sort((a,b) => (b+a)-(a+b)).join('')
  return answer[0]==='0'? '0' : answer;
}

console.log(solution(numbers2))