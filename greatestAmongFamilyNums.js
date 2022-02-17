function getGreatestFamilyNum(num){
    var theNum = Number(num.toString().split('').sort().reverse().join(''));
    return theNum > 100000000 ? -1 : theNum;
}
console.log(getGreatestFamilyNum(553));