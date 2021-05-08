function solution(n, k, cmd) {
  var answer = []
  let cutStack = []
  let current = Array(n).fill('O')
  
  for(let index in cmd) {
      let [type, value] = cmd[index].split(" ")
      switch(type) {
          case "D":
              k += parseInt(value)
              break;
          case "U":
              k -= parseInt(value)
              break;
          case "C":
              cutStack.push(k)
              if(k === current.length-1) {
                  k -= 1
              } 
              current.pop()
              break;
          case "Z":
              let p = cutStack.pop()
              if(p <= k) {
                  k++
              }
              current.push("O")
              break;
      }
      // console.log(cutStack)
  }
  let len = cutStack.length
  for(let index in len) {
      let pos = cutStack.pop()
      let before = current.slice(0,pos)
      let after = current.slice(pos)
      
      current = [...before,"X",...after]
      console.log(current)
      console.log(index)
  }
  answer = current
  return answer.join('');
}

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])