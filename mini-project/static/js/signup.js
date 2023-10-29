let container = document.getElementById('container')

toggle = () => {
	container.classList.toggle('sign-in')
	container.classList.toggle('sign-up')
}

setTimeout(() => {
	container.classList.add('sign-in')
}, 200)



gsap.from('ul.messages', {
    y: -200,
    duration: 1,
    opacity: 1
})

gsap.to('ul.messages', {
    y: -200,
    duration: 1,
    opacity: 1,
    delay: 3
})

