const analyzeBtn = document.getElementById("analyzeBtn");
const promptInput = document.getElementById("prompt");
const resultDiv = document.getElementById("result");

analyzeBtn.addEventListener("click", async () => {
  const prompt = promptInput.value.trim();
  if (!prompt) return alert("Please enter a prompt.");

  // Show loading spinner
  resultDiv.classList.remove("hidden");
  resultDiv.innerHTML = "<p>Analyzing...</p>";

  try {
    const response = await fetch("https://ai-waf-production.up.railway.app", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    console.log("BACKEND RESPONSE:", data);

    // Determine risk color
    let riskClass = "risk-low";
    if (data.risk_score >= 70) riskClass = "risk-high";
    else if (data.risk_score >= 40) riskClass = "risk-medium";

    // Display results
    resultDiv.innerHTML = `
      <p><span class="intent">Intent:</span> ${data.intent}</p>
      <p><span class="risk-score ${riskClass}">Risk Score:</span> ${data.risk_score}</p>
      <p><span class="reason">Reason:</span> ${data.reason}</p>
    `;
  } catch (err) {
    console.error(err);
    resultDiv.innerHTML = "<p style='color:red;'>Error connecting to backend.</p>";
  }
});
