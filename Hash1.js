const participant = ["leo", "kiki", "eden"];
const completion = ["eden", "kiki"];
const participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
const completion2 = ["josipa", "filipa", "marina", "nikola"]

function solution(participant, completion) {
  participant.sort()
  completion.sort()
  for(let i=0; i<participant.length; i++) {
    if (participant[i] !== completion[i]) {
      return participant[i]
    }
  }
}

const result = solution(participant2,completion2);
console.log(result)
