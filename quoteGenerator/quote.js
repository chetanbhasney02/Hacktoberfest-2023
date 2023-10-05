var quotes = {
    quote:['Be yourself,everyone else is already taken',"Two things are infinite,the universe and human stupidity,and I'm not sure about the universe",
"The way to get started is to quit talking and begin doing.","Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma,which is living with the results of other people's thinking.",
 "If life were predictable it would cease to be life, and be without flavor.","If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.","Life is what happens when you're busy making other plans.",
"Spread love everywhere you go. Let no one ever come to you without leaving happier.","When you reach the end of your rope, tie a knot in it and hang on.","Always remember that you are absolutely unique. Just like everyone else.",
"Don't judge each day by the harvest you reap but by the seeds that you plant.","The future belongs to those who believe in the beauty of their dreams.","Tell me and I forget. Teach me and I remember. Involve me and I learn.","The best and most beautiful things in the world cannot be seen or even touched,they must be felt with the heart"],
    author:['Oscar Wilde','Albert Einstein',"Walt Disney","Steve Jobs","Eleanor Roosevelt","Oprah Winfrey","James Cameron","John Lennon","Mother Teresa","Franklin D. Roosevelt","Margaret Mead","Robert Louis Stevenson","Eleanor Roosevelt","Benjamin Franklin","Helen Keller"]
}
var i = quotes.quote.length - 1;
var element = document.getElementById("changer");
var credit = document.getElementById("author")
document.getElementById("button").addEventListener("click",() => {
    element.innerText = quotes.quote[i];
    credit.innerText = "-" +quotes.author[i]
    i--;
    if (i == 0){
        i = quotes.quote.length -1;
    }
    document.getElementById("content").style.animation = "animation 2s";
})