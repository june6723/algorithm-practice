priorities = [2,2,1,1, 2, 9, 2, 3, 2, 2]
location = 1

function solution(priorities, location) {
  const myValue = priorities[location]
  let curLoc
  priorities = priorities.filter((item) => item >= myValue)
  let higher = []
  let same = []
  priorities.map((item,index) => {
    if(item > myValue) higher.push(item)
    if(item === myValue) {
      same.push(item)
      if(index === location) curLoc = same.length
    }
  })

  if(higher.length === 0) return curLoc

  const smallestValue = higher.reduce((acc,cur) => {
    return Math.min(acc,cur)
  },10)
  const lastIndex = priorities.lastIndexOf(smallestValue) 
  const before = priorities.slice(0,lastIndex).filter((item) => item === myValue).length
  const after = same.length - before

  if(before === 0 || after === 0) {
    return higher.length + curLoc
  } else {
    return higher.length + after + curLoc
  }  
}

function solution2(priorities, location) {
    var list = priorities.map((t,i)=>({
        my : i === location,
        val : t
    }));
    var count = 0;        
    while(true){
        var cur = list.shift();        
        if(list.some(t=> t.val > cur.val )){
            list.push(cur);                        
        }
        else{            
            count++;
            if(cur.my) {
              console.log(list) 
              return count;
            }
        }
    }
}

console.log(solution2(priorities,location))