function areAnagrams(str1, str2) {
  str1 = str1.toLowerCase().split("").sort().join("").trim();
  str2 = str2.toLowerCase().split("").sort().join("").trim();

  const checkAnagram = str1 === str2;
  console.log(checkAnagram);
}

areAnagrams("Astronomer", "Moon starer");
areAnagrams("School master", "The classroom");
areAnagrams("The Morse Code", "Here come dots");
areAnagrams("ant", "TEN");
