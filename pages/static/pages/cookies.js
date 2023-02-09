function writeCookie(name, value, days){
    // By default there is no expiration date for cookies.
    let expires = ''

    // Specifying a number od days makes the cookie persistent.
    if (days) {
        let date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires =" + date.toGMTString();

        // Set cookie to the name, value, and expiration date.
        document.cookie = name + '=' + value + expires + "; path=/";


    }
}

function readCookie(name){
    // Find the specifie cookie and return the name.

    let searchName= name+'=';
    let cookies =document.cookie.split(';');
    for (let i=0;i<cookies.length;i++ ){
        let c=cookies[i];
        while(c.charAt(0) == ' ')
          c=c.substring(1, c.length);
        if (c.indexOf(searchName)==0)
          return c.substring(searchName.length, c.length);  
    }
    return null;
}

function eraseCookie(name){
    // Erased the specified cookie.
    writeCookie(name,"",-1);
}

 