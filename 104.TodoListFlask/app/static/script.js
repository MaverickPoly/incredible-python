const completedClass = "flex justify-between items-center p-4 border border-green-800 rounded-lg"
const uncompletedClass = "flex justify-between items-center p-4 border border-red-800 rounded-lg"

function toggleTodo(id) {
    const baseUrl = window.location.origin;

    fetch(`${baseUrl}/todos/${id}/toggle`, {
        method: "PATCH"
    }).then((res) => res.json()).then(data => {
        const message = data["message"];

        const todoDiv = document.querySelector(`.todo${id}`)
        const isCompleted = todoDiv.classList.contains("border-green-800")

        if (isCompleted) {   
            todoDiv.className = `${uncompletedClass} todo${id}`
        } else {
            todoDiv.className = `${completedClass} todo${id}`
        }
    }).catch(err => {
        console.err(err);
    })
}

function deleteTodo(id) {
    const baseUrl = window.location.origin;

    fetch(`${baseUrl}/todos/${id}/delete`, {
        method: "DELETE"
    }).then((res) => res.json()).then(data => {
        const message = data["message"];

        const todoDiv = document.querySelector(`.todo${id}`)
        todoDiv.remove();
    }).catch(err => {
        console.err(err);
    })
}
