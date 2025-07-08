document.addEventListener('DOMContentLoaded', async function () {
    const symbols = { EUR: '€', GBP: '£', INR: '₹', USD: '$' };

    function getCookie(name) {
        return document.cookie.split('; ').reduce((r, v) => {
            const parts = v.split('=');
            return parts[0] === name ? decodeURIComponent(parts[1]) : r;
        }, '');
    }

    function setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
    }

    const savedCurrency = getCookie("currency") || "USD";
    const currencySelect = document.getElementById("currency-select");
    currencySelect.value = savedCurrency;  // Set the dropdown to the saved currency

    let rates = {};
    if (savedCurrency !== "USD") {
        try {
            const res = await fetch("/api/exchange-rates/");
            const data = await res.json();
            console.log("Full API response:", data);
            rates = data.conversion_rates || {};
            console.log("Rates object:", rates);
        } catch (error) {
            console.error("Error fetching exchange rates:", error);
        }
    }

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

            container.textContent = `${symbol} ${convertedPrice}`;
        });
    }

    updatePrices(savedCurrency);

    currencySelect.addEventListener("change", async function () {
        const selectedCurrency = this.value;
        setCookie("currency", selectedCurrency, 7);

        // Fetch new exchange rates if the currency is not USD
        if (selectedCurrency !== "USD") {
            try {
                const res = await fetch("/api/exchange-rates/");
                const data = await res.json();
                console.log("Fetched new rates:", data);
                rates = data.conversion_rates || {};
            } catch (error) {
                console.error("Error fetching new exchange rates:", error);
            }
        }

        updatePrices(selectedCurrency);
    });
});
