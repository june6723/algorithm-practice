progresses = [93, 30, 55]	
speeds = [1, 30, 5]
progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

function solution(progresses, speeds) {
  let answer = [];
  let length = progresses.length
  let release = [];
  let speedsStack = [];
  for(let i=0; i<length; i++) {
    release.push(progresses.pop())
    speedsStack.push(speeds.pop())
  }
  let doneCount = length
  for(;doneCount>0;) {
    let leftPercentage = 100-release[doneCount-1]
    let requiredDay = Math.ceil(leftPercentage/speedsStack[doneCount-1])
    for(let i=0; i<doneCount; i++){
      release[i] += requiredDay*speedsStack[i]
    }
    while(true) {
      if(release[doneCount-1] >= 100) {
        release.pop()
        doneCount -= 1
      } else {
        break;
      }
    }
    answer.push(length-doneCount)
    length = doneCount
  }
  return answer;
}

console.log(solution(progresses, speeds))