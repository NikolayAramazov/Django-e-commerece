document.addEventListener('DOMContentLoaded', async function () {
    const symbols = { EUR: '€', GBP: '£', INR: '₹', USD: '$' };

    // Function to get a cookie by name
    function getCookie(name) {
        return document.cookie.split('; ').reduce((r, v) => {
            const parts = v.split('=');
            return parts[0] === name ? decodeURIComponent(parts[1]) : r;
        }, '');
    }

    // Function to set a cookie
    function setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
    }

    // Get the currency from the cookie or default to USD
    const savedCurrency = getCookie("currency") || "USD";
    const currencySelect = document.getElementById("currency-select");
    currencySelect.value = savedCurrency;  // Set the dropdown to the saved currency

    // Fetch exchange rates only if the selected currency is not USD
    let rates = {};
    if (savedCurrency !== "USD") {
        try {
            const res = await fetch("/api/exchange-rates/");
            const data = await res.json();
            console.log("Full API response:", data); // Log the entire response object
            rates = data.conversion_rates || {}; // Use conversion_rates if that's where the rates are stored
            console.log("Rates object:", rates); // Log the rates object to see if EUR is present
        } catch (error) {
            console.error("Error fetching exchange rates:", error);
        }
    }

    // Function to update the prices
    function updatePrices(currency) {
        const priceContainers = document.querySelectorAll('[data-usd]');

        priceContainers.forEach(container => {
            const basePrice = parseFloat(container.getAttribute("data-usd"));
            const symbol = symbols[currency] || '$';
            let convertedPrice;

            if (currency === "USD") {
                convertedPrice = basePrice.toFixed(2);
            } else {
                const rate = rates[currency];
                convertedPrice = rate ? (basePrice * rate).toFixed(2) : basePrice.toFixed(2);
            }

            // Only update the text content of the container
            container.textContent = `${symbol} ${convertedPrice}`;
        });
    }

    // Initially update prices based on the saved currency
    updatePrices(savedCurrency);

    // When the currency is changed, update the prices and save the new currency in the cookie
    currencySelect.addEventListener("change", async function () {
        const selectedCurrency = this.value;
        setCookie("currency", selectedCurrency, 7); // Set cookie for 7 days

        // Fetch new exchange rates if the currency is not USD
        if (selectedCurrency !== "USD") {
            try {
                const res = await fetch("/api/exchange-rates/");
                const data = await res.json();
                console.log("Fetched new rates:", data); // Log the new rates for debugging
                rates = data.conversion_rates || {};
            } catch (error) {
                console.error("Error fetching new exchange rates:", error);
            }
        }

        // Update all product prices based on the selected currency
        updatePrices(selectedCurrency);
    });
});
