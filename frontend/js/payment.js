const API_BASE_URL = 'http://localhost:5000';

document.addEventListener('DOMContentLoaded', function() {
    const paymentForm = document.getElementById('payment-form');
    const planSelect = document.getElementById('plan');
    const payBtn = document.getElementById('pay-btn');

    // Update button text when plan changes
    planSelect.addEventListener('change', function() {
        const plan = this.value;
        const price = plan === 'premium' ? 'KES 999' : 'KES 9,900';
        payBtn.textContent = `Subscribe Now - ${price}`;
    });

    paymentForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const email = document.getElementById('email').value;
        const plan = document.getElementById('plan').value;

        if (!email) {
            alert('Please enter your email address');
            return;
        }

        payBtn.textContent = 'Processing...';
        payBtn.disabled = true;

        try {
            const response = await fetch(`${API_BASE_URL}/create-subscription`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, plan })
            });

            if (!response.ok) {
                throw new Error('Payment initialization failed');
            }

            const data = await response.json();
            
            // Redirect to InterSed payment page
            window.location.href = data.payment_url;
            
        } catch (error) {
            console.error('Payment error:', error);
            alert('Payment initialization failed. Please try again.');
        } finally {
            payBtn.textContent = planSelect.value === 'premium' ? 'Subscribe Now - KES 999' : 'Subscribe Now - KES 9,900';
            payBtn.disabled = false;
        }
    });
});