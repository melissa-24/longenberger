$(document).ready(function(){
    $('#showWork').click(function() {
        $('#hideWork').animate( {
            width: 'toggle'
        })
        $('#hideWork').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center'
        })
    })
    $('#showLearning').click(function() {
        $('#hideLearning').animate( {
            width: 'toggle'
        })
        $('#hideLearning').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center'
        })
    })
    $('#showHome').click(function() {
        $('#hideHome').animate( {
            width: 'toggle'
        })
        $('#hideHome').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center'
        })
    })
    $('#showCoding').click(function() {
        $('#hideCoding').animate( {
            width: 'toggle'
        })
        $('#hideCoding').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center'
        })
    })
})

const btn = document.querySelector('.stack')
const currentStack = localStorage.getItem('stack')
if (currentStack == 'python') {
    document.body.classList.add('ptPython')
}

btn.addEventListener('click', function() {
    document.body.classList.toggle('ptPython')
    let stack = 'webFun'
    if(document.body.classList.contains('ptPython')) {
        stack = 'python'
    }
    localStorage.setItem('stack', stack)
})
function est() {
    est = new Date().toLocaleTimeString('en-GB')
    // console.log("est: ", est)
    document.getElementById('myTime').innerText = est
}
function cst() {
    cst = new Date(new Date().getTime() + -1*60*60*1000).toLocaleTimeString('en-GB')
    console.log("cst: ", cst)
    document.getElementById('centralTime').innerText = cst
}
function pst() {
    pst = new Date(new Date().getTime() + -3*60*60*1000).toLocaleTimeString('en-GB')
    // console.log("est: ", pst)
    document.getElementById('pacificTime').innerHTML = pst
}