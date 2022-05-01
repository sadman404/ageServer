function submitAge() {
    age = document.getElementById("age").value;

    fetch('http://127.0.0.1:8000/api/age', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'age': age
        })
    }).then(res => res.json())
        .then(data => {
            isAdult = data.isAdult;
            document.getElementById("status").innerHTML = isAdult ? "You are an Adult" : "You are a kid";
        });
}