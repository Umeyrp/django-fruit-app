fetch("http://127.0.0.1:8000/fruit_app/")
    .then((response) => response.json())
    .then((data) => {
        const fruitList = document.getElementById("fruit-list");

        data.forEach((fruit) => {
            const li = document.createElement("li");

            li.textContent = `${fruit.name} - ${fruit.gewicht} - ${fruit.farbe}`;

            fruitList.appendChild(li);
        });
    });
