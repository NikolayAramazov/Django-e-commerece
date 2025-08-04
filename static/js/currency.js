document.addEventListener('DOMContentLoaded', async () => {
    const symbols = { EUR: '€', GBP: '£', INR: '₹', USD: '$' };

    const getCookie = name =>
        document.cookie.split('; ').reduce((r, v) => {
            const [k, val] = v.split('=');
            return k === name ? decodeURIComponent(val) : r;
        }, '');

    const setCookie = (name, value, days) => {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
    };

    const currencySelect = document.getElementById("currency-select");
    const savedCurrency = getCookie("currency") || "USD";
    currencySelect.value = savedCurrency;

    let rates = await getRatesIfNeeded(savedCurrency);

    function updatePrices(currency) {
        const symbol = symbols[currency] || '$';
        const priceContainers = document.querySelectorAll('[data-usd]');

        priceContainers.forEach(container => {
            const usd = parseFloat(container.getAttribute("data-usd"));
            const rate = currency === "USD" ? 1 : rates?.[currency];
            const price = (usd * (rate || 1)).toFixed(2);
            container.textContent = `${symbol} ${price}`;
        });
    }

    async function getRatesIfNeeded(currency) {
        if (currency === "USD") return {};
        try {
            const res = await fetch("/api/exchange-rates/");
            const data = await res.json();
            return data.conversion_rates || {};
        } catch (err) {
            console.error("Exchange rate fetch error:", err);
            return {};
        }
    }

    updatePrices(savedCurrency);

    currencySelect.addEventListener("change", async () => {
        const selectedCurrency = currencySelect.value;
        setCookie("currency", selectedCurrency, 7);
        rates = await getRatesIfNeeded(selectedCurrency);
        updatePrices(selectedCurrency);
    });

    window.addEventListener('pageshow', async (event) => {
    if (event.persisted) {
        const currentCurrency = getCookie("currency") || "USD";
        currencySelect.value = currentCurrency;
        rates = await getRatesIfNeeded(currentCurrency);
        updatePrices(currentCurrency);

    }
});

});
