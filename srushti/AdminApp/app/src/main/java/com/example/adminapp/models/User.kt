package com.example.adminapp.models

data class User(
    var userId: String = "",
    var fullName: String = "",
    var email: String = "",
    var mobile: String = "",
    var gender: String = "",
    var address: String = "",
    var profileImage: String = "",
    var role: String = "User",
    var status: String = "Active",
    var createdAt: Long = 0,
    var totalOrders: Int = 0
)
