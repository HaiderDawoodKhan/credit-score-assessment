document.getElementById("predictionForm").addEventListener("submit", async function(e){
    e.preventDefault();
    
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        key = key.replaceAll("_"," ");
        data[key] = value;
    });
    console.log(data)
    try {
        document.getElementById("result").textContent = `Loading...`;
        document.getElementById("explanation").textContent = ``;

        const response = await axios.post("/prediction", data);
        
        if (!response.data.error) {
            document.getElementById("result").textContent = `Credit Score Assessment: ${response.data.prediction}`;
            document.getElementById("explanation").textContent = `Explanation: ${response.data.explanation}`;
        }
        else
        {
            console.log(response.data.error);
        }
    } catch (error) {
        console.log(error.message)
    }
});
