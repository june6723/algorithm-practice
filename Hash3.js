const case1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["wea", "ww"],["weg","111"], ["bbb","ww"]]

function solution(clothes) {
  let answer = 0;
  const kinds = {};
  const kindsArr = []
  for(let i=0; i<clothes.length; i++) {
    const kind = clothes[i][1]
    if(!Object.keys(kinds).includes(kind)) {
      kinds[kind] = 1
    } else {
      kinds[kind] ++
    }
  }
  for(key in kinds) {
    kindsArr.push(kinds[key])
  }
  // console.log(kindsArr)
  function hashSum(arr, n) {
    console.log(arr, n)
    if(n===1) {
      return arr.reduce((acc, cur) => acc += cur)
    } else if(arr.length === n) {
      return arr.reduce((acc=1,cur) => acc *= cur)
    } else {
      const nextArr = arr.filter((_,index)=> index !== 0)
      return (arr[0]*hashSum(nextArr, n-1) + hashSum(nextArr, n))
    }
  }
  
  // for (let i=1; i<=kindsArr.length; i++) {
  //   answer += hashSum(kindsArr, i)
  // }
  console.log(hashSum([1,1,1,1,1,1,1,1,1,1,1,1,1],3))
  return answer;
}

console.log(solution(case1))
