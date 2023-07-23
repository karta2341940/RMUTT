let href = document.querySelectorAll(".ls a")
let arr = []
href.forEach(value => arr.push({ "title": value.innerHTML,"href":value.href }))
