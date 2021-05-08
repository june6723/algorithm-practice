numbers = [1, 1, 1, 1, 1]
target=3

function solution(numbers, target) {
  var answer = 0;
  recur(0,0)
  return answer;

  function recur(count, sum) {
    if(count === numbers.length) {
      if(sum === target) answer++
      return
    }
    
    recur(count+1, sum-numbers[count])
    recur(count+1, sum+numbers[count])
  }
}

console.log(solution(numbers,target))