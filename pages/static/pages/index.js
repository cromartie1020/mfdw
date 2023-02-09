
function setCookie(key, value, days){
    const d = new Date();
    d.setTime(d.getTime() + (days * 86400000))
    document.cookie = key + '=' + encodeURI(value) +';expires=' + d.toUTCString() + ';'

}

