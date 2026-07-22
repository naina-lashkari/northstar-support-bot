from backend.data import (
    ORDERS,
    RETURN_POLICY,
    SHIPPING,
    PRODUCTS,
    BOT_INFO
)

from backend.intents import INTENTS
WAITING_FOR_ORDER = False

def detect_intent(message: str):
    """
    Detect the user's intent based on keywords.
    """

    message = message.lower().strip()

    for intent, keywords in INTENTS.items():
        for keyword in keywords:
            if keyword in message:
                return intent

    return "fallback"


def handle_order_tracking(order_number: str):
    """
    Handle order tracking using mock order data.
    """

    if not order_number:
        return (
            "Sure! Please provide your order number (111, 222, or 333).",
            False
        )

    order_number = order_number.strip()

    if order_number in ORDERS:
        return (
            ORDERS[order_number]["message"],
            False
        )

    return (
        "Sorry, I couldn't find that order number. Please check it and try again.",
        False
    )


def handle_returns():
    return (
        "🔄 Returns & Exchanges\n\n"
        f"✅ Return Window: {RETURN_POLICY['return_window']}\n\n"
        f"✅ Item Condition:\n{RETURN_POLICY['condition']}\n\n"
        f"✅ Packaging:\n{RETURN_POLICY['packaging']}\n\n"
        "🔗 <a href='returns.html' target='_blank'>Open Returns Page</a>\n\n"
        "If you need additional help, you can also request a live agent.",
        False
    )

def handle_shipping():
    return (
        f"📦 Standard Shipping: {SHIPPING['standard']}\n\n"
        f"⚡ Expedited Shipping: {SHIPPING['expedited']}",
        False
    )


def handle_product_recommendation(user_message: str):
    message = user_message.lower()

    if "hiking" in message:
        products = PRODUCTS["hiking"]

        return (
            "🥾 Recommended Products\n\n"
            f"• {products[0]}\n"
            f"• {products[1]}\n"
            f"• {products[2]}\n\n"
            "Enjoy your hiking adventure! 🌲",
            False
        )

    elif "camp" in message or "camping" in message:
        products = PRODUCTS["camping"]

        return (
            "🏕️ Recommended Products\n\n"
            f"• {products[0]}\n"
            f"• {products[1]}\n"
            f"• {products[2]}\n\n"
            "Have a great camping trip! 🔥",
            False
        )

    elif "winter" in message or "cold" in message:
        products = PRODUCTS["winter"]

        return (
            "❄️ Recommended Products\n\n"
            f"• {products[0]}\n"
            f"• {products[1]}\n"
            f"• {products[2]}\n\n"
            "Stay warm and safe! 🧤",
            False
        )

    return (
    "I'd be happy to help you find the right product! 😊\n\n"
    "First, what type of outdoor activity are you shopping for?\n\n"
    "• Hiking 🥾\n"
    "• Camping 🏕️\n"
    "• Winter Adventures ❄️\n\n"
    "Also, are you looking for clothing, footwear, or equipment?",
    False
)


def get_bot_response(user_message: str):
    global WAITING_FOR_ORDER

    message = user_message.lower().strip()

    # If bot is waiting for an order number
    if WAITING_FOR_ORDER:

        WAITING_FOR_ORDER = False

        if message in ORDERS:
            return handle_order_tracking(message)

        return (
            "❌ Invalid order number. Please enter 111, 222, or 333.",
            False
        )

    # Greeting
    if any(keyword in message for keyword in INTENTS["greeting"]):
        return (
            f"👋 Hello! Welcome to {BOT_INFO['name']}!\n\n"
            "I'm here to help you with:\n"
            "• 📦 Order Tracking\n"
            "• 🔄 Returns & Exchanges\n"
            "• 🚚 Shipping Information\n"
            "• 🎒 Product Recommendations\n"
            "• 👨‍💼 Live Agent\n\n"
            "How can I assist you today?",
            False
        )

    # Order Tracking
    elif any(keyword in message for keyword in INTENTS["order_tracking"]):

        # User typed order number in same message
        for order_number in ORDERS.keys():
            if order_number in message:
                return handle_order_tracking(order_number)

        WAITING_FOR_ORDER = True

        return (
            "📦 Sure! Please provide your order number (111, 222, or 333).",
            False
        )

    # Returns
    elif any(keyword in message for keyword in INTENTS["returns"]):
        return handle_returns()

    # Shipping
    elif any(keyword in message for keyword in INTENTS["shipping"]):
        return handle_shipping()

    # Product Recommendation
    elif any(keyword in message for keyword in INTENTS["product_recommendation"]):
        return handle_product_recommendation(message)

    # Human Agent
    elif any(keyword in message for keyword in INTENTS["live_agent"]):
        return (
            "👨‍💼 Connecting you to a Live Agent...\n\n"
            "A support specialist will assist you shortly.\n\n"
            "Type 'menu' anytime to return to the main menu.",
            True
        )

    # Main Menu
    elif message == "menu":
        WAITING_FOR_ORDER = False

        return (
            f"👋 Welcome to {BOT_INFO['name']}!\n\n"
            "I can help you with:\n"
            "• 📦 Order Tracking\n"
            "• 🔄 Returns & Exchanges\n"
            "• 🚚 Shipping Information\n"
            "• 🎒 Product Recommendations\n"
            "• 👨‍💼 Live Agent\n\n"
            "How can I assist you today?",
            False
        )

    # Fallback
    else:
        return (
            "Sorry, I didn't understand that.\n\n"
            "You can ask about:\n"
            "• 📦 Order Tracking\n"
            "• 🔄 Returns & Exchanges\n"
            "• 🚚 Shipping Information\n"
            "• 🎒 Product Recommendations\n"
            "• 👨‍💼 Live Agent\n\n"
            "Or type 'menu' to return to the main menu.",
            False
        )