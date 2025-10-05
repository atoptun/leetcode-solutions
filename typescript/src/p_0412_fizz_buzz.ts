
function fizzBuzz(n: number): string[] {
    const result: string[] = Array(n).fill("");
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            result[i - 1] = "FizzBuzz";
        } else if (i % 3 === 0) {
            result[i - 1] = "Fizz";
        } else if (i % 5 === 0) {
            result[i - 1] = "Buzz";
        } else {
            result[i - 1] = i.toString();
        }
    }
    return result;
};

function tests() {
    let n = 3;
    let expected = ["1","2","Fizz"];
    let result = fizzBuzz(n);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test case 1 failed: fizzBuzz(${n}) = ${JSON.stringify(result)}, expected ${JSON.stringify(expected)}`);
    console.log(`Test case 1 passed: fizzBuzz(${n}) = ${JSON.stringify(result)}`);

    n = 5;
    expected = ["1","2","Fizz","4","Buzz"];
    result = fizzBuzz(n);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test case 2 failed: fizzBuzz(${n}) = ${JSON.stringify(result)}, expected ${JSON.stringify(expected)}`);
    console.log(`Test case 2 passed: fizzBuzz(${n}) = ${JSON.stringify(result)}`);

    n = 15;
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"];
    result = fizzBuzz(n);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test case 3 failed: fizzBuzz(${n}) = ${JSON.stringify(result)}, expected ${JSON.stringify(expected)}`);
    console.log(`Test case 3 passed: fizzBuzz(${n}) = ${JSON.stringify(result)}`);
}

tests();