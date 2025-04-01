const {spawn} =require('child_process');
const readline=require('readline');

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
});
let pythonProcess;
let r = 0, n =5;
let senddata= [];
senddata.push("madhyapradesh");

senddata.forEach(answer =>{
    r++;
    pythonProcess = spawn('python',['bot.py',answer]);
    pythonProcess.stdout.on('data', data => {
        console.log(`${r}th process done\n`);
    });
    pythonProcess.stderr.on('data', data => {
        console.error(`An error occured , ${data}`);
    });
});
