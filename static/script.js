
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("predictionForm");
    const result = document.getElementById("result");

    if (!form) {
        console.error("Prediction form not found. Check index.html.");
        return;
    }

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        if (result) {
            result.textContent = "Predicting...";
        }

        const formData = new FormData(form);
        const inputData = Object.fromEntries(formData.entries());

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(
                    Object.fromEntries(
                        Object.entries(inputData).map(([key, value]) => [
                            key,
                            value === "true" ? true :
                            value === "false" ? false :
                            value
                        ])
                    )
                )
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "Prediction failed");
            }

            if (result) {
                result.textContent = JSON.stringify(data, null, 2);
            }
        } catch (error) {
            if (result) {
                result.textContent = "Error: " + error.message;
            }
            console.error(error);
        }
    });
});
