document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('recommendation-form');
    const formSection = document.querySelector('.form-section');
    const resultsSection = document.getElementById('results-section');
    const resetBtn = document.getElementById('reset-btn');
    
    const clusterTitle = document.getElementById('cluster-title');
    const clusterDescription = document.getElementById('cluster-description');
    const grid = document.getElementById('recommendations-grid');

    // Define the products for each cluster
    const clusterData = {
        0: {
            title: "Cluster 0: The Balanced Shopper",
            desc: "You have moderate income and spending. We recommend our best-value everyday bundles.",
            products: [
                { icon: "🥩", name: "Fresh Meat Pack", desc: "Quality cuts for everyday meals." },
                { icon: "🍷", name: "Table Wine", desc: "Great taste at an affordable price." },
                { icon: "🛒", name: "Essential Bundle", desc: "Daily household needs." }
            ]
        },
        1: {
            title: "Cluster 1: The Premium VIP",
            desc: "High income, high spending. You appreciate the finer things in life.",
            products: [
                { icon: "🍾", name: "Vintage Champagne", desc: "Aged to perfection." },
                { icon: "✨", name: "Gold Membership", desc: "Exclusive access and rewards." },
                { icon: "🦞", name: "Gourmet Seafood", desc: "Imported and fresh." }
            ]
        },
        2: {
            title: "Cluster 2: The Smart Saver",
            desc: "Budget-conscious shopper. We have the best deals for you today!",
            products: [
                { icon: "🏷️", name: "Mega Discount Bundle", desc: "Save up to 40% on essentials." },
                { icon: "🍎", name: "Seasonal Fruits", desc: "Fresh and budget-friendly." },
                { icon: "🍬", name: "Sweet Treats", desc: "Affordable indulgences." }
            ]
        },
        3: {
            title: "Cluster 3: The Trendsetter",
            desc: "Moderate to high income with high spending. Here is what is trending right now.",
            products: [
                { icon: "🌟", name: "Trending Wines", desc: "Our most popular selections this month." },
                { icon: "🎁", name: "Curated Gift Box", desc: "Handpicked premium items." },
                { icon: "🍫", name: "Imported Chocolates", desc: "Rich and luxurious." }
            ]
        }
    };

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const income = parseFloat(document.getElementById('income').value);
        const spending = parseFloat(document.getElementById('spending').value);
        
        // Simple heuristic mimicking the KMeans model boundaries
        let clusterId = 0;
        
        if (income > 65000 && spending > 800) {
            clusterId = 1; // Premium
        } else if (income <= 45000 && spending <= 400) {
            clusterId = 2; // Budget
        } else if (income > 45000 && spending > 600) {
            clusterId = 3; // Trendsetter
        } else {
            clusterId = 0; // Balanced
        }

        displayResults(clusterId);
    });

    function displayResults(clusterId) {
        const data = clusterData[clusterId];
        
        // Update text
        clusterTitle.textContent = data.title;
        clusterDescription.textContent = data.desc;
        
        // Build product cards
        grid.innerHTML = '';
        data.products.forEach((prod, index) => {
            const card = document.createElement('div');
            card.className = `product-card`;
            card.style.animationDelay = `${index * 0.15}s`; // Staggered animation
            card.innerHTML = `
                <div class="product-icon">${prod.icon}</div>
                <h3>${prod.name}</h3>
                <p>${prod.desc}</p>
            `;
            // Add animation class after a tiny delay to ensure it triggers
            setTimeout(() => card.classList.add('animate-fade-in'), 10);
            grid.appendChild(card);
        });

        // Hide form, show results
        formSection.classList.add('hidden');
        resultsSection.classList.remove('hidden');
        resultsSection.classList.add('glass-panel', 'animate-fade-in');
    }

    resetBtn.addEventListener('click', () => {
        form.reset();
        resultsSection.classList.add('hidden');
        formSection.classList.remove('hidden');
        formSection.classList.add('animate-fade-in');
    });
});
