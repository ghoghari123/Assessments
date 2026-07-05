package com.example.adminapp.models

data class Product(
    var productId: String = "",
    var productName: String = "",
    var categoryId: String = "",
    var categoryName: String = "",
    var description: String = "",
    var originalPrice: Double = 0.0,
    var discount: Double = 0.0,
    var finalPrice: Double = 0.0,
    var stock: Int = 0,
    var productImage: String = "",
    var createdAt: Long = 0
)
