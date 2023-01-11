//Задание 1

function getMultiples(n) {
    for (let i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log("fizzbuzz");
        }
        else if (i % 3 == 0) {
            console.log("fizz");
        }
        else if (i % 5 == 0) {
            console.log("buzz");
        }
        else {
            console.log(i);
        }
    }
}


//Задание 2 (осторожно, немного адище для глаз :D)

function getGroomedString(string) {
    let groomedString = string.replace(/[^а-яА-Яa-zA-Z0-9]/g, "").toLowerCase();
    return groomedString;
}

function getReversedString(string) {
    let reversedString = string.split("").reverse().join("");
    return reversedString;
}
function checkPalindrom(string) {
    let groomedString = getGroomedString(string);
    let reversedString = getReversedString(groomedString);

    if (groomedString == reversedString) {
        console.log("Палиндром!");
    }
    else {
        console.log("Не палиндром!");
    }
}

//Задание 3. Хроники познавания Мощи Регулярных Выражений

function getVowels (string) {
    let withoutVowels = string.replace(/[?аеоуиэыaeiouy]/g, "")
    let vowelsCount = string.length - withoutVowels.length
    console.log(`Количество гласных: ${vowelsCount}`)
}
