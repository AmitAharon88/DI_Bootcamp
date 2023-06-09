// 1.
const sentence = "The movie is not that bad, I like it";

// 2.
const wordNot = sentence.indexOf("not");
console.log(wordNot);

// 3.
const wordBad = sentence.indexOf("bad");
console.log(wordBad);

// 4. Two ways to do it
if (wordBad > wordNot) {
  const modifiedSentence = sentence.replace(/not.*bad/, "good");
  console.log(modifiedSentence);
}

if (wordBad > wordNot) {
  const fullblock = sentence.slice(wordNot, wordBad + 3);
  const modifiedSentence = sentence.replace(fullblock, "good");
  console.log(modifiedSentence);
}

// 5.
if (wordBad < wordNot || (wordNot === -1 && wordBad === -1)) {
  console.log(sentence);
} else {
  console.log("Condition not met");
}
