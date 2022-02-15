// Targets the right side wrapper
let rightWrapper = document.querySelector(".right-wrapper")
// Boolean value with a default value of false
let open = false;

// When the website loads, it will run the below
window.addEventListener("load", async () => {

    // Loads the json data 
    const loadJSON = async () => {
      const data = await fetch("./assets/data.json");
      const jsonData = await data.json();
      return jsonData.rows
    }
  
    // Assigns the response to a variable named 'data'
    const data = await loadJSON();
    
    // Looping over each data in the json file
    data.forEach((data, index) => {

        // Creating a p tag for the 'content' and have it set to 'hidden' by default
        const content = document.createElement("p");
        content.setAttribute("class", "content hidden")
        content.textContent = data.content

        // The span represents the up and down arrows
        let span = document.createElement("span")
        span.textContent = "▼"
        
        // The button will be the 'title' and index. It also appends the span from above
        const btn = document.createElement("button");
        btn.textContent = `${index + 1}. ${data.title}`
        btn.append(span)

        // A div is created and wraps the button and content
        const div = document.createElement("div")
        div.append(btn)
        div.append(content)

        // The entire right wrapper appends each div
        rightWrapper.append(div)
    })

    // Selects each button/title, content questions, span and div
    const button = document.querySelectorAll("button")
    let content = document.querySelectorAll(".content");
    let span = document.querySelectorAll("span")
    let div = document.querySelectorAll("div")

    // For each question, if a user clicks on it, it will toggle the hidden class
    button.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            content[index].classList.toggle("hidden")

            // It will set the arrow to upwards if open is false and then set it to true
            if (!open) {
                span[index].textContent = "▲"
                open = true;
            } else {
                span[index].textContent = "▼"
                open = false;
            }
        })

        // I could have set border bottom in the css but it looks slightly thicker as the 'border top' and 'border bottom' collides so I did it in JS...
        // ... so that I only target the last item
        if (index == button.length - 1) {
            div[index + 1].style.borderBottom = "1px solid hsl(0deg 0% 85%)"
        }

    })
}) 


