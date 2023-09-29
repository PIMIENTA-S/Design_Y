const date = document.getElementById('date');
const promtInput = document.getElementById('promtInput')
const terminal = document.getElementById('terminal');
const terminalWindow = document.getElementById('terminalWindow');

// una vez inicia el programa el usuario sobre escribir 
promtInput.focus();
// agrega la fecha en la parte superior de la terminal
date.innerText = new Date().toDateString();
// una vez el usuaria da click sobre el recuadro de la terminal este pueda escribir de inmediato
terminalWindow.addEventListener('click', () => promtInput.focus());

promtInput.addEventListener('keydown', (event) => {
    if (event.key === "Enter") {
        enterCommand(event)
    }
})

// crear funcion enterCommand