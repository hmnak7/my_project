function print(value="", sep="<br>"){
    document.write(value + sep);
}

function print(value=""){
    const div = document.createElement("div");
    div.innerHTML = value;
    document.body.appendChild(div);
}

/*function cprint(value=""){
     console.log(value);
}*/

function cprint(...args) {
    console.log(...args)
}


        function formatDate(date) {
            const year = date.getFullYear();

            const preMonth = date.getMonth() + 1;
            const month = (preMonth<10)? '0'+preMonth: ''+preMonth

            const day = String(date.getDate()).padStart(2, '0');
            // const day = date.getDate(preDate<10)? '0'+preDate: ''+preDate

            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            const seconds = String(date.getSeconds()).padStart(2, '0');

            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        }

        function RandomInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }

        function setCookie(name, value, days) {
            let expires = "";
            if (days) {
                 let date = new Date();
                 date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                 expires = "; expires=" + date.toUTCString();
            }
                 document.cookie = name + "=" + (value || "")  + expires + "; path=/";
        }

        function getCookie(name) {
            let nameEQ = name + "=";
            let ca = document.cookie.split(';');
            for(let i=0;i < ca.length;i++) {
                let c = ca[i];
                 while (c.charAt(0)==' ') c = c.substring(1,c.length);
                if (c.indexOf(nameEQ) == 0) return     c.substring(nameEQ.length,c.length);
            }
             return null;
        }