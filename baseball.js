const readLine = require('readline');
const MAX_TRY_COUNT = 9;
const ANSWER_NUMS = [0,0,0];
let gStrikeCount;
let gBallCount;
let gTryCount;

// set answer
function setAnswer() {
  do {
    let randNum = Math.floor(Math.random() * 10000 % 1000);
    ANSWER_NUMS[2] = randNum % 10;
    ANSWER_NUMS[0] = Math.floor(randNum / 100);
    ANSWER_NUMS[1] = Math.floor((randNum % 100) / 10)
  } while (!hasDuplicateAndZeroNumber(ANSWER_NUMS))
}

const hasZero = (val) => val[0] == 0 || val[1] == 0 || val[2] == 0
const hasDuplicateAndZeroNumber = (val) => {
  return hasZero(val) || val[0] === val[1] || val[0] === val[2] || val[1] === val[2]
}
const isValidNum = (inputStr) => {
  let msg;
  if (Number.isNaN(inputStr)) {
    msg = 'Error: Type number only!';
  } else if (inputStr.length !== 3) {
    msg = 'Error: Please enter a 3 digit number';
  } else if (hasDuplicateAndZeroNumber(inputStr)) {
    msg = 'Error: Do not type same number or zero';
  }
  if (msg) {
    console.log(msg)
    return false
  }
  return true
}

const term = readLine.createInterface({
  input: process.stdin,
  output: process.stdout,
})

term.on('line', (line) => {
  if (line === 'q') {
    return endGame();
  }
  if (line === 'r') return resetGame();

  if(!isValidNum(line)) {
    return printQuestion();
  }

  for (let i = 0; i < ANSWER_NUMS.length; i++) {
    if (ANSWER_NUMS.includes(Number(line[i]))) {
      if (ANSWER_NUMS[i] === Number(line[i])) {
        gStrikeCount++;
      } else gBallCount++;
    }
  }

  if (gStrikeCount === 3 || ++gTryCount > MAX_TRY_COUNT) {
    return endGame();
  }
})

const printQuestion = () => {
  process.stdout.write("Type a 3 digit numbers(q: Quit, r: Retry): ")
  // term.output(console.log("Type a 3 digit numbers(q: Quit, r: Retry): "));
}

const endGame = () => {
  if (gStrikeCount === 3){
    console.log("Congratulation!! U Win!!")
  } else {
    return console.log('You failed')
  }
  console.log('See you later')
  term.close();
}
const resetGame = () => {
  gStrikeCount = 0
  gBallCount = 0
  gTryCount = 0
  console.clear()

  console.log('New Game Started.\n');
  printQuestion()
  setAnswer
}

resetGame()
// console.log(hasDuplicateAndZeroNumber([1,2,3]))