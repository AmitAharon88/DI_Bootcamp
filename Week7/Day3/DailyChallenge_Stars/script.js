let star = "";
for (index = 0; index < 6; index += 1) {
  console.log((star += "*"));
}

for (index = 0; index < 7; index += 1) {
  let pattern = "";
  for (star = 1; star <= index; star += 1) {
    pattern += "*";
  }
  console.log(pattern);
}
