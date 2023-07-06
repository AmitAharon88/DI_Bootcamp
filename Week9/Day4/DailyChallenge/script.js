async function getCurrency() {
  try {
    const response = await fetch(
      `https://v6.exchangerate-api.com/v6/2eb0a1f11133b40014c9f277/codes`
    );
    if (response.ok) {
      const dataCurrency = await response.json(); //PROMISE
      addToDD(dataCurrency["supported_codes"]);
    } else {
      throw new Error("issues with fetch");
    }
  } catch (error) {
    console.log("ERROR", error);
  }
}

function addToDD(rates) {
  for (let rate of rates) {
    const dataListElement = document.getElementsByClassName("dropDown");
    for (let element of dataListElement) {
      const optionElement = document.createElement("option");
      const optionText = document.createTextNode(`${rate[0]} - ${rate[1]}`);

      optionElement.setAttribute("value", rate[0]);
      optionElement.appendChild(optionText);
      element.appendChild(optionElement);
    }
  }
  button();
}

function button() {
  const buttonElement = document.querySelector("button");
  buttonElement.addEventListener("click", makeConversion);
}

async function makeConversion(event) {
  event.preventDefault();

  const dropDown1 = document.getElementById("from");
  const fromInput = dropDown1.value;

  const dropDown2 = document.getElementById("to");
  const toInput = dropDown2.value;

  const amount = document.getElementById("final");
  const amountInput = amount.value;

  try {
    const response = await fetch(
      `https://v6.exchangerate-api.com/v6/2eb0a1f11133b40014c9f277/pair/${fromInput}/${toInput}`
    );
    if (response.ok) {
      const rateObj = await response.json(); //PROMISE
      console.log(rateObj);
      const convertedAmount = (
        rateObj["conversion_rate"] * amountInput
      ).toFixed(2);
      addFinalAmount(convertedAmount, toInput);
    } else {
      throw new Error("issues with fetch");
    }
  } catch (error) {
    console.log("ERROR", error);
  }
}

function addFinalAmount(amount, finalCurrency) {
  const pElement = document.getElementById("finalAmount");
  const pText = document.createTextNode(`${amount} ${finalCurrency}`);
  pElement.appendChild(pText);
}

getCurrency();
