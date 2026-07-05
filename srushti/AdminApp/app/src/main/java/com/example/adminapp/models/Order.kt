package com.example.adminapp.models

data class Order(
    var orderId: String = "",
    var customerName: String = "",
    var customerPhone: String = "",
    var deliveryAddress: String = "",
    var orderDate: Long = 0,
    var totalProducts: Int = 0,
    var totalAmount: Double = 0.0,
    var paymentMethod: String = "Cash on Delivery",
    var status: String = "Pending"
)
