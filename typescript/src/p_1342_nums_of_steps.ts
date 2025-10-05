function numberOfSteps(num: number): number {
  if (num === 0) return 0;

  const bitLength = Math.floor(Math.log2(num)) + 1;

  let bitCount = 0;
  let n = num;
  while (n > 0) {
    bitCount += n & 1;
    n >>>= 1;
  }

  return (bitLength - 1) + bitCount;
};

function tests() {
    let num = 14;
    let expected = 6;
    let result = numberOfSteps(num);
    console.assert(result === expected, `Test case 1 failed: numberOfSteps(${num}) = ${result}, expected ${expected}`);
    console.log(`Test case 1 passed: numberOfSteps(${num}) = ${result}`);

    num = 8;
    expected = 4;
    result = numberOfSteps(num);
    console.assert(result === expected, `Test case 2 failed: numberOfSteps(${num}) = ${result}, expected ${expected}`);
    console.log(`Test case 2 passed: numberOfSteps(${num}) = ${result}`);

    num = 123;
    expected = 12;
    result = numberOfSteps(num);
    console.assert(result === expected, `Test case 3 failed: numberOfSteps(${num}) = ${result}, expected ${expected}`);
    console.log(`Test case 3 passed: numberOfSteps(${num}) = ${result}`);

    num = 0;
    expected = 0;
    result = numberOfSteps(num);
    console.assert(result === expected, `Test case 4 failed: numberOfSteps(${num}) = ${result}, expected ${expected}`);
    console.log(`Test case 4 passed: numberOfSteps(${num}) = ${result}`);
}

tests();
