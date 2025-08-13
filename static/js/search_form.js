$(document).ready(function () {
    function searchProducts() {
        const form = $('#search-form');

        $.ajax({
            url: form.attr('action') || window.location.href,
            type: form.attr('method') || 'GET',
            data: form.serialize(),
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function(response) {
                $('#product-list').html(response.html);
            },
            error: function(xhr, status, error) {
                console.error("Error:", error);
            }
        });
    }

    $('#search-form').on('submit', function(e) {
        e.preventDefault();
        searchProducts();
        return false;
    });
});
