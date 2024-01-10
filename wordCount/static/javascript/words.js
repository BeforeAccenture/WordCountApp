function countWords() {
    let textarea = document.getElementById("id_sentence");
    let wordCount = document.getElementById("words");
    let letterCount = document.getElementById("letters");
    let lineCount = document.getElementById("lines");
    
    let text = textarea.value;

    // Count words
    let words = text.match(/\b[-?(\w+)?]+\b/gi);
    wordCount.innerHTML = words ? words.length :0;

    // Count letters
    let letters = text.replace(/\s/g, "");
    letterCount.innerHTML =letters.length;

    // Count lines
    let lines = text.split(/\r|\r\n|\n/);
    lineCount.innerHTML =lines.length;
}