const quotes = [
    {
        id : 0,
        author : 'Helen Keller',
        quote : 'The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.'
    },
    {
        id : 1,
        author : 'Oscar Wilde',
        quote : 'To live is the rarest thing in the world. Most people exist, that is all.'
    },
    {
        id : 2,
        author : 'Plato',
        quote :'Be kind, for everyone you meet is fighting a hard battle.'
    },
    {
        id : 3,
        author : 'Plato',
        quote : 'Be kind, for everyone you meet is fighting a hard battle.'
    },
    {
        id : 4,
        author : 'Bennett Henry',
        quote : 'Life is tough my darling, but so are you.'
    }
]

let previousQuoteIndex;


function generateRandomQuote() {
    let randomQuoteIndex;
    do {
        randomQuoteIndex = Math.floor(Math.random() * quotes.length);
    } while (randomQuoteIndex === previousQuoteIndex);
    
    const quote = quotes[randomQuoteIndex];

    const selectElement = document.querySelector("section");
    const quoteElement = document.createElement("p");
    const authorElement = document.createElement("p");

    const quoteContent = document.createTextNode(quote['quote']);
    const authorContent = document.createTextNode(quote['author']);

    quoteElement.appendChild(quoteContent);
    authorElement.appendChild(authorContent);
    selectElement.appendChild(quoteElement);
    selectElement.appendChild(authorElement);

    previousQuoteIndex = randomQuoteIndex;
}

const buttonElement = document.querySelector('button');
buttonElement.addEventListener('click', generateRandomQuote);


generateRandomQuote();