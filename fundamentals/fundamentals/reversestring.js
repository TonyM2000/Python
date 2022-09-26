/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */


reverseoutput = ""
function reverseString(str) {
    var newStr = ""
    for (var i = str.length - 1; i >= 0; i--){
        newStr += str[i]
    }
    return newStr
}
reverseString(str4)
console.log(reverseString(str1))