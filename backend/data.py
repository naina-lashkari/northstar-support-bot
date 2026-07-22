# Mock order database

ORDERS = {
    "111": {
        "status": "Shipped",
        "message": "Your order has been shipped and is expected to arrive tomorrow."
    },
    "222": {
        "status": "Processing",
        "message": "Your order is currently being processed and will ship within 24 hours."
    },
    "333": {
        "status": "Delivered",
        "message": "Your order has already been delivered. If you have any issues, let me know."
    }
}


# Return Policy

RETURN_POLICY = {
    "return_window": "30 days",
    "condition": "Items must be unused",
    "packaging": "Original packaging is required"
}


# Shipping Information

SHIPPING = {
    "standard": "3-5 business days",
    "expedited": "1-2 business days"
}


# Product Categories

PRODUCTS = {
    "hiking": [
        "Hiking Boots",
        "Backpacks",
        "Trekking Poles"
    ],
    "camping": [
        "Camping Tents",
        "Sleeping Bags",
        "Camping Chairs"
    ],
    "winter": [
        "Insulated Jackets",
        "Thermal Gloves",
        "Winter Boots"
    ]
}


# Brand Information

BOT_INFO = {
    "name": "North Star Support Bot",
    "tone": "Friendly, helpful, outdoorsy and concise."
}