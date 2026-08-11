const API_URL = "https://85pwdb44nc.execute-api.us-east-2.amazonaws.com/";

document.addEventListener("DOMContentLoaded", async () => {
    const counterElement = document.getElementById("visit-counter");

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();

        counterElement.textContent = data.count;
    } catch (error) {
        console.error("Error al obtener el contador:", error);
        counterElement.textContent = "Contador no disponible";
    }
});
