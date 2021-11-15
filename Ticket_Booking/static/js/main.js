const t1=document.getElementById('time1');
const t2=document.getElementById('tt');
const countdown=document.getElementById('countDown');
//console.log(countdown);
//console.log(t1.textContent);
//console.log(t2.textContent);
const eventDate=Date.parse(t2.textContent)
const mycountDown=setInterval(()=>{
    const now=new Date().getTime();

    const diff=eventDate-now
    //console.log(diff)
    const d=Math.floor(eventDate/(1000*60*60*24)-(now/(1000*60*60*24)))
    //console.log(d)
    const h=Math.floor((eventDate/(1000*60*60)-(now/(1000*60*60))) %24)
    //console.log(h)
    const m=Math.floor((eventDate/(1000*60)-(now/(1000*60))) %60)
    //console.log(m)
    const s=Math.floor((eventDate/(1000)-(now/(1000))) %60)
    //console.log(s)
    if (diff>0){

        countdown.innerHTML=d+"days,"+h+"hours,"+m+"minutes,"+s+"seconds"
        }else{
            clearInterval(mycountDown);
        countdown.innerHTML="your time as elapsed"
        }
},1000);


