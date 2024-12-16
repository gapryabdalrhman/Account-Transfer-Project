
document.getElementById('transfer-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const sourceAccountId = document.getElementById('source_account_id').value;
    const targetAccountId = document.getElementById('target_account_id').value;
    const amount = document.getElementById('amount').value;

    
    const data = {
        source_account_id: sourceAccountId,
        target_account_id: targetAccountId,
        amount: amount,
    };

    
    fetch('/transfer/accounts/transfer-funds/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        const responseMessage = document.getElementById('response-message');
        if (data.message) {
            responseMessage.textContent = data.message;
            responseMessage.style.color = 'green';
        } else if (data.error) {
            responseMessage.textContent = data.error;
            responseMessage.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response-message').textContent = 'An error occurred.';
    });
});
